from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from .views import get_animals_in_json_format, cadastrar_animal, cadastrar_dono, pagina_principal, login_view, logout_view, meus_animais, animal_edit, animal_delete, animal_encontrado

urlpatterns = [
    path('cadastrar_animal', cadastrar_animal, name='cadastrar_animal'),
    path('cadastrar_dono', cadastrar_dono, name='cadastrar_dono'),
    path('meus_animais', meus_animais, name='meus_animais'),
    path('<int:id>/edit', animal_edit, name="animal_edit"),
    path('<int:id>/delete', animal_delete, name="animal_delete"),
    path('', pagina_principal, name='pagina_principal'),
    path('login', login_view, name='login'),
    path('<int:id>/animal_encontrado', animal_encontrado, name='animal_encontrado'),
    path('logout', logout_view, name='logout'),
    path('animaljson', get_animals_in_json_format, name='animal_json'),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)