from django import forms
from django.forms import ModelForm

from .models import Appointment, Income


class IncomeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Income
        fields = ["description", "value", "date"]

        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }


class AppointmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Appointment
        fields = ["patient", "age", "gender", "description", "doctor", "date"]

        widgets = {
            "gender": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Select(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
