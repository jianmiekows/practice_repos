from django.db import models
from django.core.validators import MinValueValidator

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    avatar = models.ImageField(upload_to='pokemons/avatars/', default='pokemons/avatars/avatar default.jpg')
    background = models.ImageField(upload_to='pokemons/background/', default='pokemons/background/bg default.png')



