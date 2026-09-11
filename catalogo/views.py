from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    context = {
        'titulo': 'Bienvenido a la App Catálogo',
        'descripcion': 'Esta es la página principal de la aplicación Catálogo.',
        'items': ['Item 1', 'Item 2', 'Item 3'], 
    }
    return render(request, 'catalogo/home.html', context)