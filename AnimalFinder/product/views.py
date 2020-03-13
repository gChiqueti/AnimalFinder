from django.shortcuts import render
from .models import Dono, Animal
from .forms import AnimalForm

# Create your views here.

def list_products(request):
    products = Animal.objects.all()
    return render(request, 'products.html', {'products': products})
    
    
def cadastrar_animal(request):
    form = AnimalForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'cadastrar_animal.html', {'form': form})
