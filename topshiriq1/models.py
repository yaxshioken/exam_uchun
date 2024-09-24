from fcntl import FASYNC

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model
from django.forms import IntegerField

from core.models import SoftDeleteModel


class Account(AbstractUser, SoftDeleteModel):
    phone = CharField(max_length=128)


class Vacancy(Model):
    name = CharField(max_length=128, unique=True)
    salary = CharField(max_length=128)
