from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games(request):
  games = Game.objects.all()
  return render(request, 'games.html', {'games': games})

def gameform(request):
  return render(request, 'gameform.html')

def gamesdetail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'gamesdetail.html', {'game': game})

class GameCreate(CreateView):
  model = Game
  fields = ['name', 'state', 'city', 'address', 'year', 'date', 'organizer', 'contact', 'website', 'facebook', 'description']

class GameUpdate(UpdateView):
  model = Game
  fields = ['name', 'state', 'city', 'address', 'year', 'date', 'organizer', 'contact', 'website', 'facebook', 'description']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'