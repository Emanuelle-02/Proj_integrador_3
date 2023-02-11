from django.urls import reverse
from django.utils import timezone

from apps.doutor.models import Leave

from .test_doutor_base import DoutorTestBase


class DoutorModelsTest(DoutorTestBase):
    def create_medical_leave(self, patient="Paciente1", days=2):
        return Leave.objects.create(
            patient=patient,
            doctor=self.create_test_doctor(),
            days=days,
            date=timezone.now(),
        )

    def test_expense_creation(self):
        l = self.create_medical_leave()
        self.assertTrue(isinstance(l, Leave))
        self.assertEqual(l.__str__(), l.patient)
