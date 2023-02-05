from django import forms

from .models import Category, Expenses


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ["description", "category", "value", "date"]

        widgets = {
            "description": forms.Textarea(
                attrs={"class": "form-control", "type": "text"}
            ),
            "category": forms.Select(),
            "value": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "type": "text"}),
        }
