# import requests
import datetime

from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse, reverse_lazy

from apps.accounts.models import User
from apps.administrador.models import Category, Expenses

from .test_admin_base import AdminTestBase


class AdminViewsTest(AdminTestBase):
    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")

    def test_list_doctor_view(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("list_doctor"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "medico/list_doctor.html")

    def test_list_recepcionist_view(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("list_recepcionist"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recepcionista/list_recepcionist.html")

    def test_list_income_view(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("list_caixa"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "caixa/list_caixa.html")

    def test_list_expenses_view(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("list_despesas"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "despesas/list_despesas.html")

    def test_create_category(self):
        self.create_test_user()
        self.login()
        response_200 = self.client.post(
            reverse("categoria_form"), data={"name": "Limpeza"}, follow=True
        )
        self.assertEqual(response_200.status_code, 200)

    def test_list_category_view(self):
        self.create_test_user()
        self.login()
        response = self.client.get(reverse("list_categoria"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "despesas/list_categoria.html")

    def test_create_expense(self):
        self.create_test_user()
        self.login()
        response = self.client.post(
            reverse("despesa_form"),
            data={
                "description": "Teste qualquer",
                "category": "Test",
                "value": 200,
                "date": datetime.date(2023, 2, 4),
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
