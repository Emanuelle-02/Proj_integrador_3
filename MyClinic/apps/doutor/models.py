from django.db import models
from django.utils.timezone import now

from apps.accounts.models import Doctor


# Create your models here.
class Leave(models.Model):
    patient = models.CharField(max_length=255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    days = models.IntegerField()
    date = models.DateField(default=now)

    def __str__(self):
        return self.patient
