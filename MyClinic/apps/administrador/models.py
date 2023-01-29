from django.db import models
from django.utils.timezone import now

from apps.accounts.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, default = '-------------')

    def __str__(self):
        return self.name

class Expenses(models.Model):
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    value = models.FloatField()
    date = models.DateField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description