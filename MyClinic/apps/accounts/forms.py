from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import *


class DoctorForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].label = "Nome"
        self.fields["last_name"].label = "Sobrenome"
        self.fields["username"].label = "Nome de usuário"
        self.fields["phone"].label = "Telefone"
        self.fields["city"].label = "Cidade"
        self.fields["specialization"].label = "Especialização"
        self.fields["password1"].label = "Senha"
        self.fields["password2"].label = "Confirmar senha"

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
        doctor = Doctor.objects.update_or_create(user=user)
        return user


class RecepcionistForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RecepcionistForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].label = "Nome"
        self.fields["last_name"].label = "Sobrenome"
        self.fields["username"].label = "Nome de usuário"
        self.fields["phone"].label = "Telefone"
        self.fields["city"].label = "Cidade"
        self.fields["password1"].label = "Senha"
        self.fields["password2"].label = "Confirmar senha"

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["first_name", "last_name", "username", "email", "phone", "city"]

    # @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_recepcionist = True
        user.save()
        recepcionist = Recepcionist.objects.update_or_create(user=user)
        return user
