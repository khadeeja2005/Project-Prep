from django.db import models


SEM_TYPES_CHOICES = (
    ("Non-Semestered", "Non-Semestered"),
    ("Semestered", "Semestered")
)

SCHOOL_BOARD_CHOICES = (
    ("OCDSB", "OCDSB"),
    ("OCSB", "OCSB"),
    ("N/A", "N/A")
)

class CSV_FILE(models.Model):
    names = models.TextField()
    prep_times = models.TextField()
    locations = models.TextField()

class additional_info_models(models.Model):
    sem_type = models.CharField(max_length=14, choices=SEM_TYPES_CHOICES, default="Semestered")
    start_date = models.DateField()
    end_date = models.DateField()
    school_board = models.CharField(max_length=5, choices=SCHOOL_BOARD_CHOICES, default="OCDSB")


# Create your models here.
