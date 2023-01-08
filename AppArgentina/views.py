from django.shortcuts import render
from .models import *
from django.http import HttpResponse

from AppArgentina.forms import JugadoresForm, TecnicoForm, CompeticionForm

"""def jugadores (request):
    jugador1= Jugadores(nombre="Lionel", apellido="Messi", posicion="Delantero", dorsal=10)
    jugador1.save()

    jugador2= Jugadores(nombre="Leandro", apellido="Paredes", posicion="Mediocampista", dorsal=5)
    jugador2.save()

    lista_jugadores= [jugador1, jugador2]

    equipo= jugador1.nombre+" "+jugador1.apellido+ "-" +jugador1.posicion
    return render (request, "jugadores.html", {"jugadores":lista_jugadores})"""


"""def jugadoresFormulario (request):
    if request.method== "POST":
        nombre= request.POST ["nombre"]
        apellido= request.POST ["apellido"]
        posicion= request.POST ["posicion"]
        dorsal= request.POST ["dorsal"]
        equipo= Jugadores(nombre=nombre, apellido=apellido, posicion=posicion, dorsal=dorsal)
        equipo.save()
        return render (request, "inicio.html", {"mesaje": "El equipo de la seleccion Argentina"})
    else:
        return render (request, "jugadoresFormulario.html")"""


def jugadoresFormulario (request):
    if request.method== "POST":
        form= JugadoresForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            posicion= informacion["posicion"]
            dorsal= informacion["dorsal"]
            equipo= Jugadores(nombre=nombre, apellido=apellido, posicion=posicion, dorsal=dorsal)
            equipo.save()
            return render (request, "inicio.html", {"mesaje": "El equipo de la seleccion Argentina"})
        else:
            return render (request, "jugadoresFormulario.html", {"form": form, "mensaje": "Informacion no valida"})

    else:
        formulario= JugadoresForm()
        return render (request, "jugadoresFormulario.html", {"form": formulario})


def busquedaDorsal (request):
    return render (request, "busquedaDorsal.html")


def buscar (request):
    dorsal= request.GET["dorsal"]
    if dorsal!="":
        jugadores= Jugadores.objects.filter(dorsal__icontains=dorsal)
        return render (request, "resultadosBusqueda.html", {"jugadores": jugadores})
    
    else:
        return render (request, "busquedaDorsal.html", {"mensaje": "Ingresa un dorsal para buscar un jugador!"})