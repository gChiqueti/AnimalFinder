from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from .views import cadastrar_animal, cadastrar_dono, pagina_principal, login_view, logout_view, meus_animais

urlpatterns = [
    path('cadastrar_animal', cadastrar_animal, name='cadastrar_animal'),
    path('cadastrar_dono', cadastrar_dono, name='cadastrar_dono'),
    path('meus_animais', meus_animais, name='meus_animais'),
    path('', pagina_principal, name='pagina_principal'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)