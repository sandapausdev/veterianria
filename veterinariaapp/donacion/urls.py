from django.urls import path
from donacion import views
#ESTE ARCHIVO ES NECESARIO CREARLO E IMPORTARLO EN URLS.PY DE LA APP PRINCIPAL
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("especie", views.EspecieView.as_view(), name="especie"),
    path("raza", views.RazaView.as_view(), name="raza"),
    path("mascota", views.MascotaView.as_view(), name="mascota"),
]
