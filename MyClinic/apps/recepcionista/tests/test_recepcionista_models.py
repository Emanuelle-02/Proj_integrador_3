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
