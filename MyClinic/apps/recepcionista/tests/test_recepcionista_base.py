from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

from apps.accounts.models import User


class RecepcionistTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

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
        # recepcionist = Recepcionist.objects.create(user=recepcionist)
        return recepcionist

    def login(self):
        user_logged = self.client.login(
            username="recepcionista1", password="clinica123"
        )
        return user_logged

    def tearDown(self):
        print("\nTeste finalizado")
        return super().tearDown()
