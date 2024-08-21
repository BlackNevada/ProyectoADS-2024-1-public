"""
URL configuration for inf23620241 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inf236backend.views import *
from inf236backend import views



router = DefaultRouter()
router.register(r'motor', MotorViewSet)
router.register(r'tarea', TareaViewSet)
router.register(r'sistema', SistemaViewSet)
router.register(r'componente', ComponenteViewSet)
router.register(r'camion', CamionViewSet)
router.register(r'asignacion', AsignacionViewSet)
router.register(r'incidencia', IncidenciasViewSet)

urlpatterns = [
    #Etc
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login', login),
    path('register', register),
    #Crear instancias
    path('incidencia/nueva', nuevaIncidencia),
    path('tarea/nueva', nuevaTarea),
    path('asignacion/nueva', nuevaAsignacion),
    path('motor/nueva', nuevaMotor),
    path('camion/nueva', nuevaCamion),
    #Ver instancias
    path('incidencia', obtenerIncidencias),
    path('tarea', obtenerTareas),
    path('asignacion', obtenerAsignaciones),
]

