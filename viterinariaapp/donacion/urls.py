from django.urls import path
from donacion import views
#ESTE ARCHIVO ES NECESARIO CREARLO E IMPORTARLO EN URLS.PY DE LA APP PRINCIPAL
urlpatterns = [
    path("", views.index, name="index")
]
