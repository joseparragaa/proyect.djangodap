from django.shortcuts import render

# 1. Definimos los datos base
MI_PERFIL = {
    'mi_nombre': 'Zharick García',
    'profesion': 'Futura Ingeniera de Software',
    'email': 'zintriagi@gmail.com',
    'github': 'https://github.com/ZharickGarcia2005',
    'youtube': 'https://www.youtube.com/@zharickgarcia',
    'instagram': 'https://www.instagram.com/zharick.garcia_/',
    'tiktok': 'https://www.tiktok.com/@zharick_garcia_',
}

def portada(request):
    # Usamos ** para pasar el diccionario como variables independientes al HTML
    return render(request, 'core/index.html', MI_PERFIL)

def about(request):
    context = {
        **MI_PERFIL, # Esto "desempaqueta" nombre, email, etc.
        'biografia': (
            'Nací en la ciudad de Manta el 2 de agosto de 2005. Mi camino académico inició en la '
            'Unidad Educativa Leonid Aviat (2012-2015) y continuó en la Unidad Educativa Stella Maris, '
            'donde completé mi formación secundaria en el año 2024.'
        ),
        'biografia_extra': (
            'Actualmente, me encuentro enfocada en mi formación profesional como estudiante de '
            'Ingeniería de Software en la Universidad Técnica de Manabí (UTM), cursando el quinto nivel. '
            'Me apasiona el desarrollo backend con Python y Django.'
        ),
    }
    return render(request, 'core/about.html', context)

def portfolio(request):
    proyectos = [
        {
            'titulo': 'Sistema de Identificación y Localización Canina',
            'descripcion': (
                'Aplicación móvil para la gestión de identificación en veterinarias y '
                'localización de perritos extraviados.'
            ),
            'url': '#',
            'imagen': 'home-bg.jpg',
        },
        {
            'titulo': 'Museo Virtual Interactivo',
            'descripcion': (
                'Proyecto colaborativo que permite explorar galerías y exposiciones '
                'digitales de forma inmersiva desde el navegador.'
            ),
            'url': '#',
            'imagen': 'about-bg.jpg',
        },
    ]
    context = {
        **MI_PERFIL,
        'proyectos': proyectos,
    }
    return render(request, 'core/portfolio.html', context)

def contact(request):
    context = {
        **MI_PERFIL,
        'descripcion_contacto': (
            'Como estudiante de quinto nivel en la UTM, estoy abierta a consultorías, '
            'colaboraciones en proyectos de software y prácticas profesionales.'
        ),
        'telefono': '0985999728',
        'honorarios': '50$/h',
    }