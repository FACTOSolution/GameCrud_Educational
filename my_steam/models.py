# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

class Game(models.Model):
    # Campos
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=20, help_text="Max of 20 letters", null=True)
    platform = models.CharField(max_length=20, help_text="Max of 20 letters", null=True)
    cover_img = models.ImageField(upload_to='game_covers/', default=False)

    GENRES = (
        ('ACT', 'Action'),
        ('ADV', 'Adventure'),
        ('RPG', 'Role Play Game'),
        ('RCG', 'Racing'),
    )

    genre = models.CharField(max_length=20, null=True, choices=GENRES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game-detail', args=[str(self.id)])
