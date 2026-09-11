from django.shortcuts import render

def mostrar_productos(request):
    productos = [
        {'nombre': 'Producto 1', 'precio': 10.99},
        {'nombre': 'Producto 2', 'precio': 15.49},
        {'nombre': 'Producto 3', 'precio': 7.99},
    ]
    return render(request, 'catalogo/index.html', {'productos': productos})