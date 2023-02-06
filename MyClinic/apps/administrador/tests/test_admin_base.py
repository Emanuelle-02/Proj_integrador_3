from django.contrib.auth.models import User
from django.test import TestCase

from apps.accounts.models import Doctor, User


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

    def login(self):
        user_logged = self.client.login(
            username="administrador1", password="clinica123"
        )
        return user_logged

    def tearDown(self):
        print("\nTeste finalizado")
        return super().tearDown()
