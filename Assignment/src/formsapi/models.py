from django.db import models
from datetime import date

class BogieChecksheet(models.Model):
    bogie_number = models.CharField(max_length=100)
    date_of_inspection = models.DateField(default=date.today)
    inspector_name = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Bogie #{self.bogie_number}"

class WheelSpecification(models.Model):
    wheel_number = models.CharField(max_length=100)
    bogie_number = models.CharField(max_length=100)
    diameter = models.DecimalField(max_digits=5, decimal_places=2)
    flange_thickness = models.DecimalField(max_digits=5, decimal_places=2)
    inspection_date = models.DateField(default=date.today)

    def __str__(self):
        return f"Wheel #{self.wheel_number}"