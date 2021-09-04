from typing import NamedTuple
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Game(models.Model):
  name = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  year = models.IntegerField()
  date = models.DateField('Competition Date')
  organizer = models.CharField(max_length=100, blank=True)
  contact = models.CharField(max_length=100, blank=True)
  website = models.CharField(max_length=100, blank=True)
  facebook = models.CharField(max_length=100, blank=True)
  description = models.TextField(max_length=1000, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("games_detail", kwargs={"game_id": self.id})