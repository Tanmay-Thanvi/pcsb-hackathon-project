from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class ExtendedUser(models.Model):
    user = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)
    sigs = ArrayField(models.IntegerField(), default=[])
