from operator import truediv

from django.db import models
from django.db.models import manager
from django.db.models.query import QuerySet


class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        """
        Getting queryset function for Soft Delete models.
        """
        return super().get_queryset().filter(active="true")


class SoftDeleteModel(models.Model):
    """
    Abstract model to model tables having soft-deletable objects
    """

    active = models.BooleanField(default=True)

    objects = SoftDeleteManager()
    all_objects = manager.Manager()

    def delete(self, *args, **kwargs):
        """
        Delete function for soft deleting a model object instance.
        """
        self.active = False
        self.save()

    def permanent_delete(self, *args, **kwargs):
        """
        Delete function for permanently deleting a model object instance.
        """
        super().delete(*args, **kwargs)

    class Meta:
        """Meta class for Soft Delete Model"""

        abstract = True
