# import requests
import datetime

from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse, reverse_lazy

from apps.accounts.models import User
from apps.administrador.models import Category, Expenses

from .test_doutor_base import DoutorTestBase


class DoctorViewsTest(DoutorTestBase):
    def test_doctor_index_view(self):
        self.create_test_doctor()
        self.login()
        response = self.client.get(reverse("doc_index"))
        self.assertTemplateUsed(response, "doc_index.html")

    def test_list_doctor_appointment_view(self):
        self.create_test_doctor()
        self.login()
        response = self.client.get(reverse("list_appointment"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "consulta/list_appointment.html")

    def test_list_doctor_exam_view(self):
        self.create_test_doctor()
        self.login()
        response = self.client.get(reverse("list_exam"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "exame/list_exam.html")

    def test_list_doctor_complete_appointment_view(self):
        self.create_test_doctor()
        self.login()
        response = self.client.get(reverse("list_complete_appointment"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "consulta/list_complete_appointment.html")

    def test_doc_exam_complete_view(self):
        self.create_test_doctor()
        self.login()
        response = self.client.get(reverse("list_complete_exam"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "exame/list_complete_exam.html")

    def test_list_medical_leave_view(self):
        self.create_test_doctor()
        self.login()
        response = self.client.get(reverse("list_medical_leave"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "atestado/list_leave.html")
