from rest_framework import serializers
from .models import Motor
from .models import Tarea
from .models import Sistema
from .models import Componente
from .models import Camion
from .models import Mecanico
from .models import Asignacion
from .models import Incidencia

# Serializers are in charge to render arbitrary data types (json, URL encode forms, XML's) to python-like objects
class MotorSerializer(serializers.ModelSerializer):
    # This will tell which fields django will use while processing the view.
    class Meta:
        model = Motor
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class SistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistema
        fields = '__all__'

class ComponenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Componente
        fields = '__all__'

class CamionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camion
        fields = '__all__'

class MecanicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mecanico
        fields = '__all__'

class AsignacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignacion
        fields = '__all__'

class IncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidencia
        fields = '__all__'
        read_only_fields = ['fecha']

class MecanicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mecanico
        fields = ["rut", "nombre", "password", "is_jefe_motor"]