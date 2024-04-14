from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=24)
    email = models.EmailField(max_length=24)
    password = models.CharField(max_length=24)
    confirm_password = models.CharField(max_length=24)
