# import requests
import datetime

from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse, reverse_lazy

from apps.accounts.models import User
from apps.administrador.models import Category, Expenses

from .test_recepcionista_base import RecepcionistTestBase


class RecepcionistViewsTest(RecepcionistTestBase):
    def test_recepcionist_index_view(self):
        self.create_test_recepcionist()
        self.login()
        response = self.client.get(reverse("recepcionist_index"))
        self.assertTemplateUsed(response, "recepcionist_index.html")

    def test_list_appointment_view(self):
        self.create_test_recepcionist()
        self.login()
        response = self.client.get(reverse("appointment_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "consultas/appointment_list.html")

    def test_list_exam_view(self):
        self.create_test_recepcionist()
        self.login()
        response = self.client.get(reverse("exams_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "exames/list_exams.html")
