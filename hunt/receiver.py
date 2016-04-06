from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Player


@receiver(post_save, sender=User)
def make_player_profile(sender, instance, created, **kwargs):
      if created:
          Player.objects.create(user=instance)
