from django.shortcuts import render
from tools.Auth import login
from .services.incidencias import registrar_incidencia, obtener_incidencias

# Create your views here.
@login
def viewIncidencia(request):

    if request.session['is_jefe_motor']:
        incidencias = obtener_incidencias(request)
        return render(request, 'incidenciaJefe.html', { 'enlace_acti': 'Incidencias', 'user_name': request.session['nombre'], 'incidencias': incidencias })

    return render(request, 'incidenciaMecanico.html', { 'enlace_acti': 'Incidencias', 'user_name': request.session['nombre'] })


@login
def viewNewIncidencia(request):

    if request.method == 'GET':
        if request.session['is_jefe_motor']:
            return render(request, 'newIncidencia.html', { 'enlace_acti': 'Incidencias', 'user_name': request.session['nombre']})
        
        return render(request, 'newIncidencia.html', { 'enlace_acti': 'Incidencias', 'user_name': request.session['nombre'] })
    else:
        registrar_incidencia(request)
        return render(request, 'newIncidencia.html', { 
            'enlace_acti': 'Incidencias', 
            'user_name': request.session['nombre'] }
            )