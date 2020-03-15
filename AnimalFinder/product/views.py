from django.shortcuts import render, redirect, get_object_or_404
from .models import Dono, Animal, Contato
from .forms import AnimalForm, RegistrationForm, AuthenticationForm, ContatoForm
from .forms import AnimalForm, RegistrationForm, AuthenticationForm, ContatoForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def pagina_principal(request):
    animais_cadastrados = Animal.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(animais_cadastrados, 8)
    try:
        animais_cadastrados = paginator.page(page)
    except PageNotAnInteger:
        animais_cadastrados = paginator.page(1)
    except EmptyPage:
        animais_cadastrados = paginator.page(paginator.num_pages)
    return render(request, 'pagina_principal.html', {'animais_cadastrados': animais_cadastrados})
    
    
def cadastrar_animal(request):
    form = AnimalForm(data=request.POST, files=request.FILES)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.dono = request.user
        instance.save()
                
        return redirect('pagina_principal')

    return render(request, 'cadastrar_animal.html', {'form': form})


def cadastrar_dono(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('pagina_principal')
        else:
            context['registration_form'] = form
    else: #GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'cadastrar_dono.html', context)

def logout_view(request):
    logout(request)
    return redirect('pagina_principal')


def meus_animais(request):
    animals = [i for i in Animal.objects.all() if i.dono.email==request.user.email]
    contatos = []
    for a in animals:
        contatos.append(Contato.objects.filter(animal__id=a.id))
    context = {'animais': zip(animals, contatos) }
    return render(request, 'meus_animais.html', context)

def animal_edit(request, id=None):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        user_form = AnimalForm(request.POST, instance=animal)
        if user_form.is_valid():
            user_form.save()    
            return HttpResponseRedirect(reverse('meus_animais'))
        else:
            return render(request, 'editar_animal.html', {"user_form": user_form})
    else:
        user_form = AnimalForm(instance=animal)
        return render(request, 'editar_animal.html', {"user_form": user_form})
    
def animal_delete(request, id=None):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        animal.delete()
        return HttpResponseRedirect(reverse('meus_animais'))
    else:
        context = {}
        context['user'] = animal
        return render(request, 'deletar_animal.html', context)


def animal_encontrado(request, id=None):
    context = {}
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            animal.status = 2
            animal.save()
            instance.animal = animal
            instance.save()    
            return redirect('pagina_principal')
        else:
            context['form'] = form
    else:
        context['form'] = ContatoForm(request.POST)
    return render(request, 'animal_encontrado.html', context)



def login_view(request):

     context = {}

     user = request.user
     if user.is_authenticated:
        return redirect("pagina_principal")

     if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("pagina_principal")

     else:
        form = AuthenticationForm()

     context['form'] = form
     return render(request, 'login.html', context)

    