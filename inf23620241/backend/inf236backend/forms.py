from django import forms
from .models import *


class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['titulo', 'id_mecanico', 'n_serie_motor', 'detalles', 'posible_solucion']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['id_mecanico', 'prioridad', 'estado', 'tipo', 'n_serie_motor']

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ['n_serie_motor', 'id_camion']

class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = ['n_serie', 'estado', 'anio', 'tipo']

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['id_camion', 'estado', 'patente', 'flota']
