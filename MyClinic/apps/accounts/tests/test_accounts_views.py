# import requests
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from .test_accounts_base import AccountTestBase


class AccountsViewsTest(AccountTestBase):
    def test_home_View(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "op_login.html")

    def test_login_type_view(self):
        response = self.client.get(reverse("op_login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "op_login.html")

    def test_login_admin_view(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login/login.html")

    def test_login_doctor_view(self):
        response = self.client.get(reverse("login_doctor"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login/login_doctor.html")

    def test_login_recepcionist_view(self):
        response = self.client.get(reverse("login_recepcionist"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login/login_recepcionist.html")

    def test_deve_realizar_login_admin_sem_problemas(self):
        user = self.create_test_user()
        response = self.client.post(
            reverse("login"), {"username": user.username, "password": "clinica123"}
        )

        self.assertEqual(response.status_code, 401)

    def test_nao_deve_logar_admin_senha_invalida(self):
        user = self.create_test_user()
        response = self.client.post(
            reverse("login"), {"username": user.username, "password": "senha123"}
        )

        self.assertEqual(response.status_code, 401)
        storage = get_messages(response.wsgi_request)
        self.assertIn(
            "Nome de usuário ou senha incorreta, por favor tente novamente",
            list(map(lambda x: x.message, storage)),
        )

    def test_deve_realizar_login_recepcionista_sem_problemas(self):
        user = self.create_test_recepcionist()
        response = self.client.post(
            reverse("login_recepcionist"),
            {"username": user.user.username, "password": "clinica123"},
        )
        self.assertEqual(response.status_code, 302)

    def test_nao_deve_logar_recepcionista_senha_invalida(self):
        user = self.create_test_recepcionist()
        response = self.client.post(
            reverse("login_recepcionist"),
            {"username": user.user.username, "password": "senha123"},
        )

        self.assertEqual(response.status_code, 401)
        storage = get_messages(response.wsgi_request)
        self.assertIn(
            "Nome de usuário ou senha incorreta, por favor tente novamente",
            list(map(lambda x: x.message, storage)),
        )

    def test_nao_deve_logar_recepcionista_conta_invalida(self):
        user = self.create_test_doctor()
        response = self.client.post(
            reverse("login_recepcionist"),
            {"username": user.user.username, "password": "clinica123"},
        )

        self.assertEqual(response.status_code, 401)
        storage = get_messages(response.wsgi_request)
        self.assertIn(
            "Conta inativa ou inexistente!",
            list(map(lambda x: x.message, storage)),
        )

    def test_deve_realizar_login_doutor_sem_problemas(self):
        user = self.create_test_doctor()
        response = self.client.post(
            reverse("login_doctor"),
            {"username": user.user.username, "password": "clinica123"},
        )
        self.assertEqual(response.status_code, 302)

    def test_nao_deve_logar_doutor_senha_invalida(self):
        user = self.create_test_doctor()
        response = self.client.post(
            reverse("login_doctor"),
            {"username": user.user.username, "password": "senha123"},
        )

        self.assertEqual(response.status_code, 401)
        storage = get_messages(response.wsgi_request)
        self.assertIn(
            "Nome de usuário ou senha incorreta, por favor tente novamente",
            list(map(lambda x: x.message, storage)),
        )

    def test_nao_deve_logar_doutor_conta_invalida(self):
        user = self.create_test_recepcionist()
        response = self.client.post(
            reverse("login_doctor"),
            {"username": user.user.username, "password": "clinica123"},
        )

        self.assertEqual(response.status_code, 401)
        storage = get_messages(response.wsgi_request)
        self.assertIn(
            "Conta inativa ou inexistente!",
            list(map(lambda x: x.message, storage)),
        )

    def test_logout_user(self):
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, 302)
