# from main_app.models import Game
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

class Game:
  def __init__(self, name, state, city, address, year, date, organizer, contact, description):
    self.name = name
    self.state = state
    self.city = city
    self.address = address
    self.year = year
    self.date = date
    self.organizer = organizer
    self.contact = contact
    self.description = description

gameList = [
  Game(
    'Richmond Highland Games',
    'Virginia', 
    'Richmond',
    '4200 Caroline Avenue',
    2019,
    'October 30',
    'Chuck McGluck',
    'chuck@chuck.com',
    'Scottish Festival that takes place in Richmond, Virginia.',
  )
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games(request):
  print(gameList)
  return render(request, 'games.html',
    {'games': gameList}
  )

def gameform(request):
  return render(request, 'gameform.html')

class GameCreate(CreateView):
  model = Game
  fields = ['name', 'state', 'city', 'address', 'year', 'date', 'organizer', 'contact', 'description', 'competitors', 'results']