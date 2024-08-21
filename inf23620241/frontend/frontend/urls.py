"""
URL configuration for frontend project.

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
from django.urls import path
from login.views import viewLogin
from home.views import viewHome
from incidencia.views import viewIncidencia, viewNewIncidencia
from tarea.views import viewTareas, viewNewTareas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewLogin, name='login'),
    path('login/', viewLogin, name='login'),
    path('home/', viewHome, name='home'),
    path('incidencia/', viewIncidencia, name='incidencia'),
    path('incidencia/crear', viewNewIncidencia, name='newIncidencia'),
    path('tareas/crear', viewNewTareas, name='newTareas'),
    path('tareas/', viewTareas, name='tareas'),
]
