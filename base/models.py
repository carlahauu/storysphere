from django.db import models

# Create your models here.
class Character(models.Model):
    Name = models.CharField(max_length=30, unique=True)
    Key_Events = models.CharField(max_length = 1000, unique=True)
    Personality = models.CharField(max_length=1000, unique=True)
    Physical_Traits = models.CharField(max_length=1000, unique=True)
    Notes = models.CharField(max_length=1000, unique=True, blank=True)

class Chapter(models.Model): 
    Title = models.CharField(max_length=30, unique=True)
    Plot_Points = models.CharField(max_length = 1000, unique=True)
    Characters_Involved = models.CharField(max_length=1000, unique=True)
    Notes = models.CharField(max_length=1000, unique=True, blank=True)

class World(models.Model): 
    Name = models.CharField(max_length=30, unique=True)
    Genre = models.CharField(max_length = 1000, unique=True)
    Language = models.CharField(max_length=1000, unique=True)
    Culture = models.CharField(max_length=1000, unique=True)
    Environment = models.CharField(max_length=1000, unique=True)
    Rules_Laws = models.CharField(max_length=1000, unique=True)
    History = models.CharField(max_length=1000, unique=True, blank=True)
