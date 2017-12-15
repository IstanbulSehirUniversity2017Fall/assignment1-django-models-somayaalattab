from __future__ import unicode_literals
from django.db import models


class Countries(models.Model):
        count_name = models.CharField(max_length=60)
        count_visit = models.BooleanField()



class Cities(models.Model):
    countries = models.ForeignKey(Countries, on_delete= models.CASCADE)
    city_name = models.CharField(max_length=60)

# Create your models here.
