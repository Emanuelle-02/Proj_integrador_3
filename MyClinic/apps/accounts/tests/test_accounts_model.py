# import requests
from django.urls import reverse

from apps.accounts.models import Doctor, User

from .test_accounts_base import AccountTestBase


class AccountsViewsTest(AccountTestBase):
    def test_model_doctor(self):
        doctor = self.create_test_doctor()
        self.assertEqual(
            str(doctor.user.first_name)
            + " "
            + str(doctor.user.last_name)
            + " - "
            + str(doctor.user.specialization),
            str(doctor),
        )
