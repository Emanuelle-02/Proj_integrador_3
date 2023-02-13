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

    def test_list_income_view(self):
        self.create_test_recepcionist()
        self.login()
        response = self.client.get(reverse("list_receita"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "receita/list_receita.html")

    def test_list_done_appointment_view(self):
        self.create_test_recepcionist()
        self.login()
        response = self.client.get(reverse("done_appointment_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "consultas/done_appointment_list.html")

    def test_list_done_exam_view(self):
        self.create_test_recepcionist()
        self.login()
        response = self.client.get(reverse("exams_done_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "exames/list_done_exams.html")

    def test_income_create_view(self):
        self.create_test_recepcionist()
        self.login()
        response = self.client.post(
            reverse("receita_form"),
            data={
                "description": "Teste Income",
                "value": 200,
                "date": datetime.date(2023, 2, 12),
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_income_update_view(self):
        income = self.create_exam()
        income_update = {
            "description": "Teste Put Income",
            "value": 180,
            "date": datetime.date(2023, 2, 12),
        }
        response = self.client.post(reverse_lazy('receita_form', kwargs={"pk":income.pk}),income_update,follow=True)
        assert response.status_code == 200

    def test_appointment_create_view(self):
        self.create_test_recepcionist()
        self.login()
        response = self.client.post(
            reverse("appointment_form"),
            data={
                "patient": "Julieta",
                "age": "10",
                "doctor": self.create_test_doctor(),
                "date": datetime.date(2023, 2, 12),
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_appointment_update(self):
        appoint = self.create_exam()
        appoint_update = {
            "patient": "Julieta B.",
            "age": "11",
            "date":datetime.date.today()
        }
        response = self.client.post(reverse_lazy('appointment_form', kwargs={"pk":appoint.pk}),appoint_update,follow=True)
        assert response.status_code == 200


    def test_exam_create_view(self):
        self.create_test_recepcionist()
        self.login()
        response = self.client.post(
            reverse("exam_form"),
            data={
                "patient": "Julieta",
                "age": "10",
                "doctor": self.create_test_doctor(),
                "date": datetime.date(2023, 2, 12),
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_exam_update(self):
        exam = self.create_exam()
        exam_update = {
            "patient": "Julieta V.",
            "age": "11",
            "date":datetime.date.today()
        }
        response = self.client.post(reverse_lazy('exam_form', kwargs={"pk":exam.pk}),exam_update,follow=True)
        assert response.status_code == 200

    def test_remove_income(self):
        income = self.create_income()
        response = self.client.delete(
            reverse("delete_receita", kwargs={"pk": income.pk}), follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_remove_appointment(self):
        appoint = self.create_appointment()
        response = self.client.delete(
            reverse("delete_appointment", kwargs={"pk": appoint.pk}), follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_remove_exam(self):
        exam = self.create_exam()
        response = self.client.delete(
            reverse("delete_exam", kwargs={"pk": exam.pk}), follow=True
        )
        self.assertEqual(response.status_code, 200)
