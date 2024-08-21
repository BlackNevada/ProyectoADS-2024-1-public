from django.shortcuts import render, redirect
from tools.Auth import login

# Create your views here.
@login
def viewHome(request):
    
    if request.session['is_jefe_motor']:
        return render(request, 'homeJefe.html', { 'enlace_acti': 'Inicio', 'user_name': request.session['nombre'] })
    else:
        return render(request, 'homeMecanico.html', { 'enlace_acti': 'Inicio', 'user_name': request.session['nombre'] })