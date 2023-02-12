from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger

from apps.accounts.models import User
from apps.administrador.models import Category, Expenses


class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")
    password = Faker("password")

    class Meta:
        model = User


class CategoryFactory(DjangoModelFactory):
    name = Faker("text")

    class Meta:
        model = Category
        django_get_or_create = ["name"]


class ExpenseFactory(DjangoModelFactory):
    description = Faker("name")
    category = SubFactory(CategoryFactory)
    value = FuzzyInteger(1, 1000)
    date = Faker("date_object")
    user = SubFactory(UserFactory)

    class Meta:
        model = Expenses
        django_get_or_create = ["description"]
