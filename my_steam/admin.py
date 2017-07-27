# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmmin(admin.ModelAdmin):
    list_display = ('title','platform','genre')
    list_filter = ('platform','genre')
