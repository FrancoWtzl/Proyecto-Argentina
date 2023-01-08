from django import forms


class TecnicoForm (forms.Form):
    nombre= forms.CharField(label= "Nombre Tecnico", max_length=50)
    apellido= forms.CharField(label= "Apellido Tecnico", max_length=50)
    puesto= forms.CharField(label= "Puesto Tecnico", max_length=50)


class JugadoresForm (forms.Form):
    nombre= forms.CharField(label= "Nombre Jugador", max_length=50)
    apellido= forms.CharField(label= "Apellido Jugador", max_length=50)
    posicion= forms.CharField(label= "Posicion Jugador", max_length=50)
    dorsal= forms.IntegerField(label= "Dorsal")


class CompeticionForm (forms.Form):
    nombre= forms.CharField(label= "Nombre Competicion", max_length=50)
    pais= forms.CharField(label= "Pais Competicion", max_length=50)