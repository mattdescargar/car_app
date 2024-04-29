# car_app/models.py

from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)  # Add this line if not already present
    color = models.CharField(max_length=50)
    position = models.IntegerField()

    def __str__(self):
        return self.name
