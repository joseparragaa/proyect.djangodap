from django.urls import path
from . import views

urlpatterns = [
    path('',            views.portada,   name='portada'),
    path('about/',      views.about,     name='about'),
    path('portafolio/', views.portfolio, name='portfolio'),  # ← name='portfolio'
    path('contactos/',  views.contact,   name='contact'),
]