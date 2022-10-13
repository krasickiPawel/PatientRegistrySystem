from django.db import models
from ..authentication.models import User
from django.contrib.postgres.fields import ArrayField


class Appointment(models.Model):
    """Model definition for Appointment."""

    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient")
    date = models.DateTimeField()
    duration = models.DurationField()  # may change to integer if easier
    patient_appeared = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "appointments"
        ordering = ["-date"]


class Request(models.Model):
    """Model definition for Request."""

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient")
    symptoms = ArrayField(models.CharField(max_length=255))
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "requests"
        ordering = ["-date"]


# possible TODO: add a model for prescriptions if too few models
