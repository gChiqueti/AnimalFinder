from django.contrib import admin
from .models import Dono, Animal, Contato

@admin.register(Dono)
class UserAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Animal)
admin.site.register(Contato)
# Register your models here.
