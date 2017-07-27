# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Game
from django.views import generic

class GameListView(generic.ListView):
    model = Game
    context_object_name = 'game_list'

    def get_context_data(self, **kwargs):
        context = super(GameListView,self).get_context_data(**kwargs)
        context['extra_data'] = 'Example'
        return context

def index(request):
    num_games = Game.objects.all().count()
    return render(request, 'index.html', context={'num_games':num_games})
