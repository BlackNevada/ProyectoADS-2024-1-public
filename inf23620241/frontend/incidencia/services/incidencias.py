from django.contrib import messages
import requests
import os

def registrar_incidencia(request):
    API_URL = os.getenv('API_URL')
    token = os.getenv('TOKEN')
    response = requests.put(f'{API_URL}/incidencia/nueva', json={
        "id_mecanico": request.session['rut'],
        "titulo": request.POST['titulo'],
        "detalles": request.POST['descripcion'],
        "n_serie_motor": request.POST['n_serie'],
        "posible_solucion": "aun no hay solucion",
    })

    if response.status_code == 200:
        print('Incidencia registrada')
        messages.success(request, 'Incidencia registrada')
    else:
        print('Error al registrar incidencia')
        messages.error(request, 'Error al registrar incidencia')


def obtener_incidencias(request):
    print("Obteniendo incidencias...")
    API_URL = os.getenv('API_URL')
    token = os.getenv('TOKEN')
    response = requests.get(f'{API_URL}/incidencia/')
    if response.status_code == 200:
        return response.json()
    else:
        return None