from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import *


class DoctorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
            "city",
            "specialization",
        ]

    # @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        return user


class RecepcionistForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["first_name", "last_name", "username", "email", "phone", "city"]

    # @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_recepcionist = True
        user.save()
        return user
