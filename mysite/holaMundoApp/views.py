from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return HttpResponse( """
    <h1>Hola Mundo!!!</h1>
    <p>Esta es mi primera aplicación con Django mostrando HTML</p>
    """
)
