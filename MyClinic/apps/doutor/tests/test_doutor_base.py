from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from apps.accounts.models import User


class DoutorTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def create_test_doctor(self):
        doctor = User.objects.create_user(
            first_name="doctor1",
            last_name="D.",
            email="doctor@gmail.com",
            username="doctor1",
            city="Pau dos Ferros",
            phone="98765-4321",
            specialization="Pediatra",
        )
        doctor.set_password("clinica123")
        doctor.is_doctor = True
        doctor.save()
        # doctor = Doctor.objects.create(user=doctor)
        return doctor

    def login(self):
        user_logged = self.client.login(username="doctor1", password="clinica123")
        return user_logged

    def tearDown(self):
        print("\nTeste finalizado")
        return super().tearDown()
