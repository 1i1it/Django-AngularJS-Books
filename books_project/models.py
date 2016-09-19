from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(User)