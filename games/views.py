from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# Create your views here.




   
def index(request):
    games = Game.objects.all()

    context = {'games': games}

    return render(request, 'index.html', context) 

    

def rules(request):
    game_types = GameType.objects.all()

    context = {'game_types': game_types}

    return render(request, 'rules.html', context) 

def game_type(request, game_type_id=None):
    game_type = GameType.objects.get(id=game_type_id)

    context = {'game_type': game_type}

    return render(request, 'game_type.html', context) 

    
def new_game(request):
    game_types = GameType.objects.all()
    players = Player.objects.all()

    context = {'game_types': game_types, 'players': players}

    return render(request, 'new_game.html', context) 


def start_game(request):
    game_types = GameType.objects.all()
    players = Player.objects.all()

    context = {'game_types': game_types, 'players': players}

    return render(request, 'new_game.html', context) 