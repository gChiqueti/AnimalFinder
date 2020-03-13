from django.urls import path
from .views import cadastrar_animal, pagina_principal

urlpatterns = [
    path('', cadastrar_animal, name='cadastrar_animal'),
    path('pagina_principal', pagina_principal, name='pagina_principal'),
]
