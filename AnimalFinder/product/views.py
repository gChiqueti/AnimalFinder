from django.shortcuts import render, redirect
from .models import Dono, Animal
from .forms import AnimalForm, DonoForm

# Create your views here.

def pagina_principal(request):
    animais_cadastrados = Animal.objects.all()
    return render(request, 'pagina_principal.html', {'animais_cadastrados': animais_cadastrados})
    
    
def cadastrar_animal(request):
    form = AnimalForm(data=request.POST, files=request.FILES)

    if form.is_valid():
        form.save()
        return redirect('pagina_principal')

    return render(request, 'cadastrar_animal.html', {'form': form})


def cadastrar_dono(request):
    form = DonoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('pagina_principal')

    return render(request, 'cadastrar_dono.html', {'form': form})

def login(request):
    form = DonoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('pagina_principal')

    return render(request, 'cadastrar_dono.html', {'form': form})

    