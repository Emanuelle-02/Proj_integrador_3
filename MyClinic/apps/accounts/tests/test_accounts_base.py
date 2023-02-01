from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from apps.accounts.models import Doctor, User


class AccountTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def create_test_user(self):
        admin = User.objects.create_user(
            username="administrador1", email="admin1@gmail.com"
        )
        admin.set_password("clinica123")
        admin.save()
        return admin

    def create_test_recepcionist(self):
        recepcionist = User.objects.create_user(
            first_name="recepcionist",
            last_name="R.",
            email="recepcion@gmail.com",
            username="recepcionista1",
            city="Encanto",
            phone="91587-4569",
        )
        recepcionist.set_password("clinica123")
        recepcionist.is_recepcionist = True
        recepcionist.save()
        return recepcionist

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
        doctor = Doctor.objects.create(user=doctor)
        return doctor

    def tearDown(self):
        print("\nTeste finalizado")
        return super().tearDown()
