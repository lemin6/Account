from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=16, unique=True)
    last_name = models.CharField(max_length=16, unique=True)
    birth_date = models.DateField()
