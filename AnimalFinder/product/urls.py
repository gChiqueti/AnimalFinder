from django.urls import path
from .views import cadastrar_animal

urlpatterns = [
    path('', cadastrar_animal, name='cadastrar_animal'),
]
