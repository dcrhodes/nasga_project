from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('games/', views.games, name='games'),
  path('games/create/', views.gameform, name='game_create'),
  path('games/<int:game_id>/', views.gamesdetail, name='gamesdetail'),
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
  path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
]