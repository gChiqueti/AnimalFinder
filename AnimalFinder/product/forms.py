from django import forms
from .models import Dono, Animal, Contato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['foto',
                  'nome', 
                  'idade',
                  'cidade_desaparecimento',
                  'estado_desaparecimento',
                  'status']
                  
                  
class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome',
                  'telefone' 
                   ]
               
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Dono
        fields = ("email", "username", "telefone", "password1", "password2")
        
        
class AuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Dono
		fields = ['email', 'password']

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")


