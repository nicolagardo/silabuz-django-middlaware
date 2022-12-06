from ipware import get_client_ip
from django.http import HttpResponse
from django.shortcuts import render

BLACK_LIST = [
    '127.0.0.1'
]

def ip_is_valid(get_response):
    
    def middleware(request):
        ip, is_routeable  = get_client_ip(request)
        c ={
            "status":404
        }

        if ip in BLACK_LIST:
            return render(request, "404.html", c)
        else:
            response = get_response(request)

        return response
    
    return middleware
tarea = """
Crea un middleware que en el caso de estar baneada la ip del servidor,
 retorne una nueva vista basada en un template con un 404.
"""