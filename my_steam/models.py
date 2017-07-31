# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    steam_id = models.CharField(max_length=255, blank=True)
    steam_username = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()        

class Game(models.Model):
    # Campos
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=20, help_text="Max of 20 letters", null=True)
    platform = models.CharField(max_length=20, help_text="Max of 20 letters", null=True)
    cover_img = models.ImageField(upload_to='game_covers/', default=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

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
