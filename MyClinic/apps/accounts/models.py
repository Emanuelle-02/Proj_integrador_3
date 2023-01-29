from django.contrib.auth.models import AbstractUser
from django.db import models

SPECIALIZATION_CHOICES = (
    ("Pediatra", "Pediatra"),
    ("Gastroenterologista", "Gastroenterologista"),
    ("Neurologista", "Neurologista"),
    ("Ginecologista", "Ginecologista"),
    ("Cardiologista", "Cardiologista"),
    ("Nefrologista", "Nefrologista"),
    ("Urologista", "Urologista"),
)

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_recepcionist = models.BooleanField(default=False)
    city = models.CharField(max_length=155) 
    phone = models.CharField(max_length=16) 
    specialization = models.CharField(max_length=255, choices = SPECIALIZATION_CHOICES, default = '-------------')

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return '%s %s - %s'%(self.user.first_name, self.user.last_name, self.user.specialization)