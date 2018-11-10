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
    locations = Location.objects.all()

    context = {'game_types': game_types, 'players': players, 'locations': locations}

    return render(request, 'new_game.html', context) 


def start_game(request):
    game_types = GameType.objects.all()
    players = Player.objects.all()

    context = {'game_types': game_types, 'players': players}

    return render(request, 'new_game.html', context) 


def games(request):
    games = Game.objects.all()

    context = {'games': games}

    return render(request, 'games.html', context) 


def players(request):
    players = Player.objects.all()

    context = {'players': players}

    return render(request, 'players.html', context) 

def game(request, pk=None):
    if request.method == 'GET':
        game = Game.objects.get(id = pk)
    elif request.method == 'POST':
        game_type = GameType.objects.get(id = request.POST['game_type'])
        location = Location.objects.get(id = request.POST['location'])
        player_1 = Player.objects.get(id = request.POST['player_1'])
        player_2 = Player.objects.get(id = request.POST['player_2'])
        game = Game.objects.create(game_type = game_type, 
                                   location = location, 
                                   notes = request.POST['notes'], 
                                   player_1 = player_1, 
                                   player_2 = player_2)

    context = {'game': game}

    return render(request, 'game.html', context) 