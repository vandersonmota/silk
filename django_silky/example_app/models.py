from django.db import models

# Create your models here.
from django.db.models import TextField, BooleanField

class Product(models.Model):

    class Meta:
        abstract = True


class Blind(Product):

    name = TextField()
    child_safe = BooleanField()