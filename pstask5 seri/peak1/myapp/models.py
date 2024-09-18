from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    rol = models.IntegerField()
    city = models.CharField(max_length=100)