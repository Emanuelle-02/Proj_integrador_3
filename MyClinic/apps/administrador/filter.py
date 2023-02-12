from django import forms
from django_filters import CharFilter, ChoiceFilter, FilterSet

from apps.accounts.models import User

choices = (
    ("Pediatra", "Pediatra"),
    ("Gastroenterologista", "Gastroenterologista"),
    ("Neurologista", "Neurologista"),
    ("Ginecologista", "Ginecologista"),
    ("Cardiologista", "Cardiologista"),
    ("Nefrologista", "Nefrologista"),
    ("Urologista", "Urologista"),
)


class DoctorFilter(FilterSet):
    first_name = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    specialization = ChoiceFilter(
        choices=choices, widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["first_name", "specialization"]
