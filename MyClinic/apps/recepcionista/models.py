from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from apps.accounts.models import Doctor, User

# Create your models here.
GENDER_CHOICES = (
    ("Feminino", "Feminino"),
    ("Masculino", "Masculino"),
)

APPOINTMENT_CHOICES = {
    ("Consulta", "Consulta"),
    ("Consulta e Exame", "Consulta e Exame"),
    ("Retorno", "Retorno"),
}


CATEGORY_CHOICES = {
    ("Consulta", "Consulta"),
    ("Exame", "Exame"),
    ("Consulta e Exame", "Consulta e Exame"),
}


class Income(models.Model):
    description = models.TextField()
    value = models.FloatField()
    date = models.DateField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_income = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="----------"
    )

    def __str__(self):
        return self.description


class Appointment(models.Model):
    patient = models.CharField(max_length=255)
    age = models.CharField(max_length=3)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default="----------"
    )
    description = models.CharField(
        max_length=20, choices=APPOINTMENT_CHOICES, default="----------"
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=5)
    status = models.BooleanField(default=False)
    sintoms = models.TextField(default="A informar...")
    medication = models.TextField(default="A informar...")
    exam = models.TextField(default="A informar...")

    def __str__(self):
        return self.patient

    # def get_absolute_url(self):
    #    return reverse('detalhes:appointment_datail',)


class Exam(models.Model):
    patient = models.CharField(max_length=255)
    age = models.CharField(max_length=3)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default="----------"
    )
    type = models.TextField(default="A informar...")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=5)
    status = models.BooleanField(default=False)
