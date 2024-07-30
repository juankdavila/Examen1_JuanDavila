from django.shortcuts import render
from rest_framework import viewsets
from.serializer import FutbolistaSerializer,EquiposSerializer,Historico_EquipoSerializer
from .models import Futbolista,Equipos,Historico_Equipo



class FutbolistaViewSet(viewsets.ModelViewSet):
    queryset=Futbolista.objects.all()
    serializer_class=FutbolistaSerializer
    
class EquiposViewSet(viewsets.ModelViewSet):
    queryset=Equipos.objects.all()
    serializer_class=EquiposSerializer
    
class Historico_EquipoViewSet(viewsets.ModelViewSet):
    queryset=Historico_Equipo.objects.all()
    serializer_class=Historico_EquipoSerializer
    




