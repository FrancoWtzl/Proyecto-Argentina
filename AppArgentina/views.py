from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def jugadores (request):
    jugador1= Jugadores(nombre="Lionel", apellido="Messi", posicion="Delantero")
    jugador1.save()

    jugador2= Jugadores(nombre="Leandro", apellido="Paredes", posicion="Mediocampista")
    jugador2.save()

    lista_jugadores= [jugador1, jugador2]

    equipo= jugador1.nombre+" "+jugador1.apellido+ "-" +jugador1.posicion
    return render (request, "jugadores.html", {"jugadores":lista_jugadores})


