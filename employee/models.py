from django.db import models
from menu.models import Menu


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    voted_for = models.ForeignKey(Menu, null=True, default=None, on_delete=models.SET_NULL)
