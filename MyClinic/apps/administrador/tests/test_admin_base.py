import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from apps.accounts.models import Doctor, User
from apps.administrador.models import Category, Expenses


class AdminTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def create_test_user(self):
        admin = User.objects.create_user(
            username="administrador1", email="admin1@gmail.com"
        )
        admin.set_password("clinica123")
        admin.save()
        return admin

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

    def create_category(self, name="Eletricidade"):
        return Category.objects.create(name=name)

    def create_expense(self):
        expense = Expenses.objects.create(
            description="Teste qualquer",
            category=self.create_category(),
            value=200,
            date=datetime.date(2023, 2, 11),
            user=self.create_test_user(),
        )
        return expense

    def login(self):
        user_logged = self.client.login(
            username="administrador1", password="clinica123"
        )
        return user_logged

    def tearDown(self):
        print("\nTeste finalizado")
        return super().tearDown()
