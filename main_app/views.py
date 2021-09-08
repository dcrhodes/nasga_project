from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game
from . import forms, models

def home(request):
  return render(request, 'home.html')

def sport(request):
  return render(request, 'sport.html')

def about(request):
  return render(request, 'about.html')

class Login(LoginView):
  template_home = 'login.html'

def games(request):
  games = Game.objects.all()
  return render(request, 'games.html', {'games': games})

def game_form(request):
  return render(request, 'game_form.html')

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games_detail.html', {'game': game})

class GameCreate(CreateView):
  model = Game
  fields = ['name', 'state', 'city', 'address', 'year', 'date', 'organizer', 'contact', 'website', 'facebook', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GameUpdate(UpdateView):
  model = Game
  fields = ['name', 'state', 'city', 'address', 'year', 'date', 'organizer', 'contact', 'website', 'facebook', 'description']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)