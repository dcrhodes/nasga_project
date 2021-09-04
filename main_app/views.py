# from main_app.models import Game
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game

# class Game:
#   def __init__(self, name, state, city, address, year, date, organizer, contact, description):
#     self.name = name
#     self.state = state
#     self.city = city
#     self.address = address
#     self.year = year
#     self.date = date
#     self.organizer = organizer
#     self.contact = contact
#     self.description = description

# gameList = [
#   Game(
#     'Richmond Highland Games',
#     'Virginia', 
#     'Richmond',
#     '4200 Caroline Avenue',
#     2019,
#     'October 30',
#     'Chuck McGluck',
#     'chuck@chuck.com',
#     'Scottish Festival that takes place in Richmond, Virginia.',
#   ),
# ]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games(request):
  games = Game.objects.all()
  return render(request, 'games.html', {'games': games})

# def games(request):
#   print(gameList)
#   return render(request, 'games.html',
#     {'games': gameList}
#   )

def gameform(request):
  return render(request, 'gameform.html')

def gamesdetail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'gamesdetail.html', {'game': game})

class GameCreate(CreateView):
  model = Game
  fields = ['name', 'state', 'city', 'address', 'year', 'date', 'organizer', 'contact', 'description']