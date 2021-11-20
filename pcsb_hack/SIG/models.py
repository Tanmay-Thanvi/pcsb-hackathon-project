from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class SIG(models.Model):
    signame = models.CharField(max_length=100)
    sigdesc = models.TextField()
    sigdomain = models.CharField(max_length=100)
    numbers = models.IntegerField()
    mentor = ArrayField(models.IntegerField(), default=[])
    date = models.DateField()

class coursecontent(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    links = models.URLField(max_length=200)
    belongs = models.IntegerField(default=0)

class announcement(models.Model):
    announcement = models.TextField()
    sigid = models.IntegerField()
    by = models.CharField(max_length=100)

class classroom(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    location = models.CharField(max_length=200)
    sigid = models.IntegerField(default=0)