from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from donacion.models import Donacion, Mascota, Especie, Raza
# Create your views here.

class IndexView(generic.ListView):
    template_name = "donacion/index.html"
    context_object_name = "lista_de_donaciones"
    def get_queryset(self):
        return  Donacion.objects.order_by("-fecha_donacion")[:10]
    
class EspecieView(generic.ListView):
    template_name = "donacion/especie.html"
    context_object_name = "lista_de_especies"
    def get_queryset(self):
        return  Especie.objects.order_by("nombre_especie")[:10]

class RazaView(generic.ListView):
    template_name = "donacion/raza.html"
    context_object_name = "lista_de_razas"
    def get_queryset(self):
        return  Raza.objects.order_by("nombre_raza")[:10]

class MascotaView(generic.ListView):
    template_name = "donacion/mascota.html"
    context_object_name = "lista_de_mascotas"
    def get_queryset(self):
        return  Mascota.objects.order_by("nombre_mascota")[:10]








#def index(request):
#    return HttpResponse("Estas en la pagina principal de donaciones")

#def especie(request):
#    return HttpResponse("Estas en la pagina de especies de mascotas")

#def raza(request):
#    return HttpResponse("Estas en la pagina de razas de mascotas")

#def mascota(request):
#    return HttpResponse("Estas en la pagina de mascotas")




