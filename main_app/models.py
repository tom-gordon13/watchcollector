from django.db import models
from django.urls import reverse


# Types of servicing appointments
TYPES = (
    ('G', 'General Maintenance'),
    ('R', 'Mechanical Repairs'),
    ('S', 'Strap Replacement')
)

class Watch(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.make} - {self.model} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs= {'watch_id': self.id})


class Servicing(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    date = models.DateField('Servicing Date')
    cost = models.PositiveIntegerField()
    type = models.CharField(
        max_length=1,
        choices=TYPES,
        default=TYPES[0][0]
    )


    def __str__(self):
        return f'{self.get_type_display()} - ${self.cost}'