from django.shortcuts import render, redirect
import os
import requests

# Create your views here.

def viewLogin(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        API_URL = os.getenv('API_URL')

        rut = request.POST['rut']
        password = request.POST['password']
        response = requests.get(f'{API_URL}/login', json={ 'rut': rut, 'password': password })
        if response.status_code == 200:

            data = response.json()
            token = data['token']
            nombre = data['user']['nombre']
            rut = data['user']['rut']
            is_jefe_motor = data['user']['is_jefe_motor']

            request.session['token'] = token
            request.session['nombre'] = nombre
            request.session['rut'] = rut
            request.session['is_jefe_motor'] = is_jefe_motor

            return redirect('/home/')

        else:
            context = { 'error': 'Credenciales incorrectas' }
            return render(request, 'login.html', context)