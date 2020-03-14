from django.contrib import admin
from .models import Dono, Animal

@admin.register(Dono)
class UserAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Animal)
# Register your models here.
