from django.db import models

# Create your models here.

class Specialty(models.Model):
    name = models.CharField(max_length=255)
    specialty_id = models.CharField(unique=True, max_length=255)

class Region(models.Model):
    name = models.CharField(max_length=255)
    region_id = models.CharField(unique=True, max_length=255)