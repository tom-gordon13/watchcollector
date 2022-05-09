from django.db import models

# Create your models here.

class Watch(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.make} - {self.model} ({self.id})'