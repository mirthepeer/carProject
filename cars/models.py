from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=30)
    year = models.IntegerField()
    milage = models.IntegerField(default=500)
    def __str__(self):
        return f"Car is {self.brand} Year: {self.year} Milage is {self.milage} pk is {self.pk}"