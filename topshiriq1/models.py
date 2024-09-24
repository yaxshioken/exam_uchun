from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, CharField, DateTimeField, Model
from django.utils import timezone


class SoftDeleteModel(Model):
    is_deleted = BooleanField(default=False)
    deleted_at = DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Account(AbstractUser, SoftDeleteModel):
    phone = CharField(max_length=128)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()


class Vacancy(Model):
    name = CharField(max_length=128, unique=True)
    salary = CharField(max_length=128)
