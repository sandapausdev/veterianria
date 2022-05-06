from django.contrib import admin
from donacion.models import Especie, Raza, Donacion, Mascota

# Register your models here.
admin.site.register(Especie)
admin.site.register(Raza)
admin.site.register(Donacion)
admin.site.register(Mascota)