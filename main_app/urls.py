from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('games/', views.games, name='games'),
  # path('games/create/', views.gameform, name='game_create')
]