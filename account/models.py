from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_proof = models.ImageField(upload_to="idprof")
    phone = models.IntegerField()


 
    

    def __str__(self):
        return str(self.user)