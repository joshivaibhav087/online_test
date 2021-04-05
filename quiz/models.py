from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt


# Create your models here.
class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    python = encrypt(models.CharField(max_length=100))
    c = encrypt(models.CharField(max_length=100))
    java = encrypt(models.CharField(max_length=100))


    def __str__(self):
        return str(self.user) 