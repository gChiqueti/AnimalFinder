from django import forms
from .models import Dono, Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['foto',
                  'nome', 
                  'idade',
                  'cidade_desaparecimento',
                  'estado_desaparecimento',
                  'status']
                  
                  
class DonoForm(forms.ModelForm):
    class Meta:
        model = Dono
        fields = ['nome',
                  'email',
                  'telefone',
                  'senha'
                  ]