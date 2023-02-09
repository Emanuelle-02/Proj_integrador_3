from django import forms
from django.forms import ModelForm

from apps.recepcionista.models import Appointment


class AppointmentPrescriptionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentPrescriptionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Appointment
        fields = [
            "patient",
            "age",
            "date",
            "sintoms",
            "medication",
            "exam",
        ]

        widgets = {
            "gender": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Select(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
