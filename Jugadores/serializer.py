from rest_framework import serializers
from .models import Futbolista,Equipos,Historico_Equipo


class FutbolistaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Futbolista
        fields ='__all__'
        
class EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipos
        fields ='__all__'
        
class Historico_EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Historico_Equipo
        fields ='__all__'
        

    