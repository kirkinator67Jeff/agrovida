from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/', include('agrovida_sistema.urls')),
]

