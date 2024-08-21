from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import *
from .serializers import *
from .forms import *
from datetime import datetime, date

# Create your views here.
# Views are in charge of the business logic of the application
# Class ModelViewSet gives us many easy access to CRUD operations (Instead of creating it ourselves)

class MotorViewSet(viewsets.ModelViewSet):
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class SistemaViewSet(viewsets.ModelViewSet):
    queryset = Sistema.objects.all()
    serializer_class = SistemaSerializer

class ComponenteViewSet(viewsets.ModelViewSet):
    queryset = Componente.objects.all()
    serializer_class = ComponenteSerializer

class CamionViewSet(viewsets.ModelViewSet):
    queryset = Camion.objects.all()
    serializer_class = CamionSerializer

class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer

class IncidenciasViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer





#Login y Registro
@api_view(['GET'])
def login(request):
    rut = request.data.get('rut')
    password = request.data.get('password')
    user = authenticate(rut=rut, password=password)

    if user is None:
        return Response({'error': 'Credenciales inválidas'}, status=400)
    
    token, create = Token.objects.get_or_create(user=user)
    serializer = MecanicoSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['POST'])
def register(request):
    serializer = MecanicoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        mecanico = Mecanico.objects.get(rut=request.data.get('rut'))
        mecanico.nombre = request.data.get('nombre')
        mecanico.set_password(request.data.get('password'))
        mecanico.is_jefe_motor = request.data.get('is_jefe_motor')
        mecanico.save()

        token = Token.objects.create(user=mecanico)

        return Response({'token': token.key, "user": serializer.data})
    else:
        return Response(serializer.errors, status=400)





#Nuevas Incidencias, Tareas y Asignaciones
def validarGuardar(form, serializer_class):
    if form.is_valid():
        instance = form.save()
        serializer = serializer_class(instance)
        return Response(serializer.data, status=200)
    else:
        return Response({'error': 'Algunos campos no fueron completados correctamente', 'details':form.errors}, status=400)

@api_view(['PUT'])
def nuevaIncidencia(request):
    form = IncidenciaForm(request.data, instance=Incidencia())
    return validarGuardar(form, IncidenciaSerializer)

@api_view(['PUT'])
def nuevaTarea(request):
    form = TareaForm(request.data, instance=Tarea())
    return validarGuardar(form, TareaSerializer)

@api_view(['PUT'])
def nuevaAsignacion(request):
    form = AsignacionForm(request.data, instance=Asignacion())
    return validarGuardar(form, AsignacionSerializer)

@api_view(['PUT'])
def nuevaMotor(request):
    form = MotorForm(request.data, instance=Motor())
    return validarGuardar(form, MotorSerializer)

@api_view(['PUT'])
def nuevaCamion(request):
    form = CamionForm(request.data, instance=Camion())
    return validarGuardar(form, CamionSerializer)





#Lista de items en Incidencias, Tareas y Asignaciones
def parseFecha(parametros):
    try:
        fecha1 = parametros["inicio"]
        fecha2 = parametros["final"]
    except:
        return {'error': 'No se han entregado los argumentos requeridos'}
    
    try:
        inicio = datetime.strptime(fecha1, '%Y-%m-%d').date()
        final = datetime.strptime(fecha2, '%Y-%m-%d').date()
        return {'inicio': inicio, 'final': final}
    except:
        return {'error': 'No se pudo obtener la fecha'}

@api_view(['GET'])
def obtenerIncidencias(request):
    parametros=request.query_params.dict()
    fecha=parseFecha(parametros)
    if 'error' in fecha:
        return Response(fecha, status=400)
    try:
        instancias = Incidencia.objects.filter(fecha__range=[fecha["inicio"], fecha["final"]])
        serializer = IncidenciaSerializer(instancias, many=True)
        return Response(serializer.data, status=200)
    except:
        return Response({'error': 'Error al buscar las instancias en la BD. Quizás no entregó los valores requeridos'}, status=400)

@api_view(['GET'])
def obtenerTareas(request):
    parametros=request.query_params.dict()
    fecha=parseFecha(parametros)
    if 'error' in fecha:
        return Response(fecha, status=400)
    try:
        instancias = Tarea.objects.filter(fecha_inicio__range=[fecha["inicio"], fecha["final"]])
        if 'rut' in parametros:
            instancias = instancias.filter(id_mecanico=parametros['rut'])
        serializer = TareaSerializer(instancias, many=True)
        return Response(serializer.data, status=200)
    except:
        return Response({'error': 'Error al buscar las instancias en la BD. Quizás no entregó los valores requeridos'}, status=400)

@api_view(['GET'])
def obtenerAsignaciones(request):
    parametros=request.query_params.dict()
    fecha=parseFecha(parametros)
    if 'error' in fecha:
        return Response(fecha, status=400)
    try:
        instancias = Asignacion.objects.filter(fecha__range=[fecha["inicio"], fecha["final"]])
        serializer = AsignacionSerializer(instancias, many=True)
        return Response(serializer.data, status=200)
    except:
        return Response({'error': 'Error al buscar las instancias en la BD. Quizás no entregó los valores requeridos'}, status=400)





#Redireccionamiento y cambiar el status de tarea a terminada
def tareasViewHandler(request):
    if request.method == 'GET':
        obtenerTareas(request)
    if request.method == 'POST':
        cambiarTarea(request)
    else:
        return Response({'error': 'metodo no soportado'}, status=400)

@api_view(['PUT'])
def cambiarTarea(request):
    parametros=request.POST
    try:
        instancias = Tarea.objects.filter(id_mecanico=parametros['id_tarea']).update(estado=parametros['nuevo_estado'])
        serializer = TareaSerializer(instancias, many=True)
        return Response(serializer.data, status=200)
    except:
        return Response({'error': 'error al cambiar el estado de la tarea, es posible que haya rellenado mal los campos'}, status=400)


