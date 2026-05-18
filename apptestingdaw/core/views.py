from django.shortcuts import render

# 1. Definimos tus datos base actualizados
MI_PERFIL = {
    'mi_nombre': 'Jose Parraga',
    'profesion': 'Estudiante de Ingeniería en Software',
    'email': 'jparraga8288@utm.edu.ec',
    'github': 'https://github.com/joseparragaa',
    'youtube': 'https://www.youtube.com/@boahancock8613',
    'instagram': 'https://www.instagram.com/a.scarinito/',
    'tiktok': 'https://www.tiktok.com/@scarinitoo',
}


def portada(request):
    # Usamos ** para pasar el diccionario como variables independientes al HTML
    return render(request, 'core/index.html', MI_PERFIL)


def about(request):
    context = {
        **MI_PERFIL,  # Esto "desempaqueta" tu nombre, email, redes, etc.
        'biografia': (
            'Soy estudiante de Ingeniería en Software. Si deseas contactarme para proyectos, '
            'dudas o simplemente hablar sobre programación, puedes encontrar mis datos a continuación.'
        ),
        'biografia_extra': (
            'Nací en la ciudad de Portoviejo el 7 de junio de 2005. Actualmente me encuentro '
            'enfocado en mi desarrollo académico y profesional, adquiriendo habilidades en la '
            'creación de soluciones tecnológicas y software de calidad.'
        ),
    }
    return render(request, 'core/about.html', context)


def portfolio(request):
    proyectos = [
        {
            'titulo': 'Juego de Ajedrez',
            'descripcion': (
                'Desarrollo de un juego de ajedrez interactivo. Ideal para practicar '
                'lógica, estrategias de juego y aplicar reglas del ajedrez tradicional.'
            ),
            'url': '#',  # Aquí puedes colocar el enlace más tarde
            'imagen': 'ajedrez.jpg',  # Recuerda tener esta imagen en tus archivos estáticos
        },
        {
            'titulo': 'Calculadora Web',
            'descripcion': (
                'Una aplicación de calculadora funcional para realizar operaciones matemáticas '
                'básicas y avanzadas con una interfaz limpia y amigable.'
            ),
            'url': '#',  # Aquí puedes colocar el enlace más tarde
            'imagen': 'calculadora.jpg',  # Recuerda tener esta imagen en tus archivos estáticos
        },
    ]

    # Combinamos tus datos de perfil con la lista de proyectos para el portafolio
    context = {
        **MI_PERFIL,
        'proyectos': proyectos
    }
    return render(request, 'core/portfolio.html', context)