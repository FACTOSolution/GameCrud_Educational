# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Game
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class GameListView(generic.ListView):
    model = Game
    context_object_name = 'game_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(GameListView,self).get_context_data(**kwargs)
        context['extra_data'] = 'Example'
        return context

class GameDetailView(generic.DetailView):
    model = Game

class GameUpdateView(UpdateView):
    model = Game
    fields = ['title','publisher','platform','cover_img','genre']

class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy('games')

def index(request):
    num_games = Game.objects.all().count()
    return render(request, 'index.html', context={'num_games':num_games})
