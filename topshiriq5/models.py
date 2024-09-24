from django.db import models
from django.db.models import ManyToManyField

from topshiriq1.models import Account

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user=models.ForeignKey(Account, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
