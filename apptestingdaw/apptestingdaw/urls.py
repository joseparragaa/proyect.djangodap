from django.contrib import admin
from django.urls import path, include # Agregamos include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # Aquí conectamos con el archivo que acabas de crear
]