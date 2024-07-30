from django.urls import path,include
from rest_framework import routers
from Jugadores import views


router=routers.DefaultRouter()
router.register(r'Futbolista',views.FutbolistaViewSet)
router.register(r'Equipos',views.EquiposViewSet)
router.register(r'Historico_Equipo',views.Historico_EquipoViewSet)



urlpatterns = [
    path('', include(router.urls)),
   
   
    
]
