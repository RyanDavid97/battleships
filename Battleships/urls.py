"""Battleships URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from Battleships.battleships import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/games/index', views.api_games_index),
    path('api/1.0/games/register/<name>', views.api_games_register),
    path('api/1.0/<name>/add/<name1>&<name2>', views.api_games_add),
    path('api/1.0/games/delete/<name>', views.api_games_delete),
    path('api/1.0/players/index', views.api_players_index),
    path('api/1.0/players/register/<name>', views.api_players_register),
    path('api/1.0/players/delete/<name>', views.api_players_delete),

]
