from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from .views import cadastrar_animal, cadastrar_dono, pagina_principal

urlpatterns = [
    path('cadastrar_animal', cadastrar_animal, name='cadastrar_animal'),
    path('cadastrar_dono', cadastrar_dono, name='cadastrar_dono'),
    path('', pagina_principal, name='pagina_principal'),
    path('login', pagina_principal, name='login'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)