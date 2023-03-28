from django.db import models

class CSV_FILE(models.Model):
    names = models.TextField()
    prep_times = models.TextField()
    locations = models.TextField()

# Create your models here.
