from django.urls import reverse
from django.utils import timezone

from apps.doutor.models import Leave

from .test_doutor_base import DoutorTestBase


class DoutorModelsTest(DoutorTestBase):
    def test_expense_creation(self):
        l = self.create_medical_leave()
        self.assertTrue(isinstance(l, Leave))
        self.assertEqual(l.__str__(), l.patient)
