# Create your views here.
# mascotasApp/views.py

from django.shortcuts import render

def mascotas(request):
    return render(request, 'index.html', {})
