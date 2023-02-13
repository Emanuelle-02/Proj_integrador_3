from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from django.utils import timezone

from apps.accounts.models import Doctor, User
from apps.doutor.models import Leave
from apps.recepcionista.models import Appointment, Exam


class DoutorTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def create_test_doctor(self):
        doctor = User.objects.create_user(
            first_name="doctor1",
            last_name="R.",
            email="doctor1@gmail.com",
            username="doctor1",
            city="Encanto",
            phone="91587-4569",
        )
        doctor.set_password("clinica123")
        doctor.is_doctor = True
        doctor.save()
        doctor = Doctor.objects.create(user=doctor)
        return doctor

    def create_medical_leave(self, patient="Paciente1", days=2):
        return Leave.objects.create(
            patient=patient,
            doctor=self.create_test_doctor(),
            days=days,
            date=timezone.now(),
        )

    def create_test_recepcionist(self):
        user = User.objects.create_user(
            first_name="recepcionist",
            last_name="R.",
            email="recepcion@gmail.com",
            username="recepcionista1",
            city="Encanto",
            phone="91587-4569",
        )
        user.set_password("clinica123")
        user.is_recepcionist = True
        user.save()
        # user = Recepcionist.objects.create(user=user)
        return user

    def create_appointment(self, patient="Paciente2", age=250):
        return Appointment.objects.create(
            patient=patient,
            age=age,
            doctor=self.create_test_doctor(),
            date=timezone.now(),
            user=self.create_test_recepcionist(),
        )

    def create_appointment(self, patient="Paciente2", age=250):
        return Appointment.objects.create(
            patient=patient,
            age=age,
            doctor=self.create_test_doctor(),
            date=timezone.now(),
            user=self.create_test_recepcionist(),
        )

    def create_exam(self, patient="Paciente7", age=28):
        return Exam.objects.create(
            patient=patient,
            age=age,
            doctor=self.create_test_doctor(),
            date=timezone.now(),
            user=self.create_test_recepcionist(),
        )

    def login(self):
        user_logged = self.client.login(username="doctor1", password="clinica123")
        return user_logged

    def tearDown(self):
        print("\nTeste finalizado")
        return super().tearDown()
