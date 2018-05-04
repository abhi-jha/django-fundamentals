from django.shortcuts import render

# Create your views here.

from gameplay.models import Game

def home(request):
    return render(request, 'player/home.html',{'ngames': Game.objects.count()})