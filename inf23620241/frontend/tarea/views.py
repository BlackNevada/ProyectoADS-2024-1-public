from django.shortcuts import render
from tools.Auth import login

# Create your views here.
@login
def viewTareas(request):
    return render(request, 'tareas.html', { 'enlace_acti': 'Tareas', 'user_name': request.session['nombre'] })

@login
def viewNewTareas(request):
    return render(request, 'newTarea.html', { 'enlace_acti': 'Tareas', 'user_name': request.session['nombre'] })