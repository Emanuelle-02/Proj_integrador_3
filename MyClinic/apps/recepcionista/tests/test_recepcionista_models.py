from django.urls import reverse
from django.utils import timezone

from apps.recepcionista.models import Appointment, Income

from .test_recepcionista_base import RecepcionistTestBase


class RecepcionistaModelsTest(RecepcionistTestBase):
    def test_income_creation(self):
        income = self.create_income()
        self.assertTrue(isinstance(income, Income))
        self.assertEqual(income.__str__(), income.description)


    def test_appointment_creation(self):
        appoint = self.create_appointment()
        self.assertTrue(isinstance(appoint, Appointment))
        self.assertEqual(appoint.__str__(), appoint.patient)
