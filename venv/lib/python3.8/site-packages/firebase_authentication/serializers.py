from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import User

__all__ = "UserSerializer",


class UserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(required=True)
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'display_name',
            'phone_number',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'new_password',
            'confirm_new_password',
        )

    def validate(self, attrs):
        if self.context['request'].method == "POST":
            if attrs.get('new_password') != attrs.get('confirm_new_password'):
                raise serializers.ValidationError({
                    "new_password": _("Passwords are not equal."),
                    "confirm_new_password": _("Passwords are not equal."),
                })
            attrs.pop('confirm_new_password')
            attrs['password'] = attrs.pop('new_password')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
