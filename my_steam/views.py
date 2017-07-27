# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Game

def index(request):
    num_games = Game.objects.all().count()
    return render(request, 'index.html', context={'num_games':num_games})
