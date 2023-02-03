# import requests
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from .test_admin_base import AdminTestBase


class AccountsViewsTest(AdminTestBase):
    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")
