from django.urls import reverse
from django.utils import timezone

from apps.recepcionista.models import Appointment, Income

from .test_recepcionista_base import RecepcionistTestBase


class RecepcionistaModelsTest(RecepcionistTestBase):
    def create_income(self, description="Exame", value=250):
        return Income.objects.create(
            description=description,
            value=value,
            date=timezone.now(),
            user=self.create_test_recepcionist(),
        )

    def test_income_creation(self):
        income = self.create_income()
        self.assertTrue(isinstance(income, Income))
        self.assertEqual(income.__str__(), income.description)

    def create_appointment(self, patient="Paciente2", age=250):
        return Appointment.objects.create(
            patient=patient,
            age=age,
            doctor=self.create_test_doctor(),
            date=timezone.now(),
            user=self.create_test_recepcionist(),
        )

    def test_appointment_creation(self):
        appoint = self.create_appointment()
        self.assertTrue(isinstance(appoint, Appointment))
        self.assertEqual(appoint.__str__(), appoint.patient)
