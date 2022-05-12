from django.db import models
from django.urls import reverse


# Types of servicing appointments
TYPES = (
    ('G', 'General Maintenance'),
    ('R', 'Mechanical Repairs'),
    ('S', 'Strap Replacement'),
)

TYPES_COMP = (
    ('M', 'Movement'),
    ('S', 'Strap'),
    ('C', 'Crystal'),
)

SUBTYPES_COMP = (
        ('MQ', 'Quartz'),
        ('MA', 'Automatic'),
        ('MM', 'Manual'),
        ('SL', 'Leather'),
        ('SM', 'Metal'),
        ('CA', 'Acrylic'),
        ('CM', 'Mineral'),
        ('CS', 'Sapphire'),
)

class Component(models.Model):
    type_comp = models.CharField(
        max_length=1,
        choices=TYPES_COMP,
        default=TYPES[0][0]
    )
    subtype_comp = models.CharField(
      max_length=2,
      choices=SUBTYPES_COMP,
    )

    def __str__(self):
        return f'{self.get_type_comp_display()}'

 


class Watch(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    components = models.ManyToManyField(Component)

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

    class Meta:
        ordering = ['-date']