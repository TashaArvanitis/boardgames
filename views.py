from django.shortcuts import render
from .models import GameSite


# Create your views here.
def index_view(request):
    template_name = 'boardgames/index.html'

    games = GameSite.objects.all()
    played_games = GameSite.objects.filter(have_played=True)
    unplayed_games = GameSite.objects.filter(have_played=False)
    return render(request, template_name, {
        'played_games': played_games,
        'unplayed_games': unplayed_games,
    })
