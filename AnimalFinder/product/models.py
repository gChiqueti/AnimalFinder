from django.db import models
from .choices import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_delete
from django.dispatch import receiver

class DonoManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Usuário precisa ter um email")
        if not username:
            raise ValueError("Usuário precisa ter um nome")
            
        user = self.model(
                email = self.normalize_email(email),
                username=username,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password):
        user=self.create_user(
            email=self.normalize_email(email), 
            username=username, 
            password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Dono(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", unique=True, max_length=100)
    username = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20) 
    date_joined = models.DateTimeField(verbose_name="date_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = DonoManager()
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
  
  
class Animal(models.Model):
    foto  = models.ImageField()
    nome  = models.CharField(max_length=100)
    idade = models.CharField(max_length=3, blank=True)
    cidade_desaparecimento = models.CharField(max_length=50)
    estado_desaparecimento = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS_ANIMAL, default=1, blank=True)  
    dono = models.ForeignKey(Dono, on_delete=models.CASCADE,  null=True)
    informacoes_extras = models.CharField(max_length=250, blank=True)
    
    def __str__(self):
        return self.nome
  

@receiver(post_delete, sender=Animal)
def submission_delete(sender, instance, **kwargs):
    instance.foto.delete(False)   

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nome    
