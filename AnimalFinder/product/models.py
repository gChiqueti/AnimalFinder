from django.db import models
from .choices import *

# Create your models here.    
class Dono(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    telefone = models.IntegerField(blank=True)
    senha = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.nome
    
class Animal(models.Model):
    foto  = models.ImageField(upload_to='profile_image', blank=True)
    nome  = models.CharField(max_length=100, blank=True)
    idade = models.CharField(max_length=3, blank=True)
    cidade_desaparecimento = models.CharField(max_length=50, blank=True)
    estado_desaparecimento = models.CharField(max_length=50, blank=True)
    status = models.IntegerField(choices=STATUS_ANIMAL, default=1)
    
    def __str__(self):
        return self.nome
    