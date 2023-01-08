from django.urls import path
from AppArgentina.views import *


urlpatterns = [
    
    path("jugadoresFormulario/", jugadoresFormulario, name= "jugadoresFormulario"),
    path("busquedaDorsal/", busquedaDorsal, name= "busquedaDorsal"),
    path("buscar/", buscar, name= "buscar"),
]