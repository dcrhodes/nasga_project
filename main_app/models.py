from typing import NamedTuple
from django.db import models

class Game(models.Model):
  name = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  year = models.IntegerField()
  date = models.DateField('Competition Date')
  organizer = models.CharField(max_length=100)
  contact = models.CharField(max_length=100)
  description = models.TextField(max_length=1000)

  def __str__(self):
    return self.name