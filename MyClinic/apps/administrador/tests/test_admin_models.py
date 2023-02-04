from django.urls import reverse
from django.utils import timezone

from apps.administrador.models import Category, Expenses

from .test_admin_base import AdminTestBase


class AdminModelsTest(AdminTestBase):
    def create_category(self, name="Eletricidade"):
        return Category.objects.create(name=name)

    def test_category_creation(self):
        cat = self.create_category()
        self.assertTrue(isinstance(cat, Category))
        self.assertEqual(cat.__str__(), cat.name)

    def create_expense(self, description="Nova despesa", value = 10):
        return Expenses.objects.create(description=description, category= self.create_category(), value=value, date=timezone.now(), user=self.create_test_user())

    def test_expense_creation(self):
        e = self.create_expense()
        self.assertTrue(isinstance(e, Expenses))
        self.assertEqual(e.__str__(), e.description)
