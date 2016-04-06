from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User,primary_key = True)
    level = models.PositiveSmallIntegerField(default=1)

    def levelup(self):
        self.level+=1


class Question(models.Model):
    level = models.PositiveSmallIntegerField()
    text = models.TextField()
    answer = models.CharField(max_length = 50)

    def save_question(self):
        self.save

    def __str__(self):
        return self.text

from .receiver import *
