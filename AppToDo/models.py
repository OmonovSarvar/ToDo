from django.db import models
from django.utils import timezone


# Create your models here.
class todomodel(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=111)
    date = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return "Yangi vazifa qoshildi"
