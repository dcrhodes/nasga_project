from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('sport/', views.sport, name='sport'),
  path('games/', views.games, name='games'),
  path('login/', views.Login.as_view(), name='login'),
  path('accounts/signup/', views.signup, name='signup'),
  path('games/create/', views.GameCreate.as_view(), name='games_create'),
  path('games/<int:game_id>/', views.games_detail, name='games_detail'),
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
  path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
]