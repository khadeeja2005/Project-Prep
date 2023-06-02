from django.db import models

# Choices for semester types for the Additional Information form
SEM_TYPES_CHOICES = (
    ("Non-Semestered", "Non-Semestered"),
    ("Semestered", "Semestered")
)

# Choices for school board for the Additional Information form
SCHOOL_BOARD_CHOICES = (
    ("OCDSB", "OCDSB"),
    ("OCSB", "OCSB"),
    ("N/A", "N/A")
)

# Section to create models

# Models declared for CSV file uploading
class CSV_FILE(models.Model):
    names = models.TextField()
    prep_times = models.TextField()
    locations = models.TextField()

# Models declared for Additional Information form
class additional_info_models(models.Model):
    sem_type = models.CharField(max_length=14, choices=SEM_TYPES_CHOICES, default="Semestered")
    start_date = models.DateField()
    end_date = models.DateField()
    school_board = models.CharField(max_length=5, choices=SCHOOL_BOARD_CHOICES, default="OCDSB")

