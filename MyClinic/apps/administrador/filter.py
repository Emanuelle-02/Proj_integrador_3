from django import forms
from django_filters import CharFilter, ChoiceFilter, FilterSet

from apps.accounts.models import User

from .constants import USER_MEDICO, USER_RECEPCIONISTA


class DoctorFilter(FilterSet):
    specialization = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    # medico = ChoiceFilter(
    #    choices=USER_MEDICO, widget=forms.Select(attrs={"class": "form-control"})
    # )

    class Meta:
        model = User
        fields = ["specialization"]


class RecepcionistFilter(FilterSet):
    description = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    recepcionista = ChoiceFilter(
        choices=USER_RECEPCIONISTA, widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["first_name", "recepcionista"]
