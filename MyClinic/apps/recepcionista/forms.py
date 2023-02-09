from django import forms
from django.forms import ModelForm

from .models import Appointment, Exam, Income


class IncomeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Income
        fields = ["description", "type_income", "value", "date"]

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


class ExamForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Exam
        fields = ["patient", "age", "gender", "type", "doctor", "date"]

        widgets = {
            "gender": forms.Select(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
