# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Game
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import AddGameForm, UserRegistrationForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError

class GameListView(LoginRequiredMixin, generic.ListView):
    model = Game
    context_object_name = 'game_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(GameListView,self).get_context_data(**kwargs)
        context['extra_data'] = 'Example'
        return context

class UserGamesList(LoginRequiredMixin, generic.ListView):
    model = Game
    context_object_name = 'game_list'

    def get_queryset(self):
        return Game.objects.filter(owner=self.request.user)

class GameCreateView(LoginRequiredMixin,CreateView):
    model = Game
    form_class = AddGameForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(GameCreateView, self).form_valid(form)

class GameDetailView(LoginRequiredMixin,generic.DetailView):
    model = Game

class GameUpdateView(LoginRequiredMixin,UpdateView):
    model = Game
    fields = ['title','publisher','platform','cover_img','genre']

class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = reverse_lazy('games')

def index(request):
    num_games = Game.objects.all().count()
    return render(request, 'index.html', context={'num_games':num_games})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user_obj = form.cleaned_data
            username = user_obj['username']
            email = user_obj['email']
            password = user_obj['password']
            if not (User.objects.filter(username=username).exists() or
                User.objects.filter(email=email).exists()):
                user = User.objects.create_user(username, email, password)
                profile_form = ProfileForm(request.POST, instance = user.profile)
                if profile_form.is_valid():
                    profile_form.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise ValidationError('Username with tath email or password' +
                    ' already exists')
    else:
        form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'user_form.html', {'form' : form, 'profile_form' :  profile_form})
