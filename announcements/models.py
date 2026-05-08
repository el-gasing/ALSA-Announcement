from django.db import models

from .departments import DEPARTMENT_CHOICES


class Participant(models.Model):
    nim = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=32, choices=DEPARTMENT_CHOICES)

    class Meta:
        ordering = ['nim']

    def __str__(self):
        return f'{self.nim} - {self.name}'
