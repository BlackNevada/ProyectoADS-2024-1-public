from django.shortcuts import redirect

def login(funcion):
    def wrapper(request):
        if 'token' not in request.session:
            return redirect('login')
        return funcion(request)
    return wrapper