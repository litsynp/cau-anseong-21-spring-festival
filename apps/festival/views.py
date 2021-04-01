from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('festival/index.html')
    context = {
        'contents': [
            {
                'name': 'Test',
                'popup': False,
                'url': 'https://www.cau.ac.kr/',
                'x': 1025,
                'y': 180,
            },
            {
                'name': 'Test',
                'popup': False,
                'url': 'https://www.cau.ac.kr/',
                'x': 830,
                'y': 250,
            },
            {
                'name': 'Test',
                'popup': False,
                'url': 'https://www.cau.ac.kr/',
                'x': 1025,
                'y': 400,
            },
            {
                'name': 'Test',
                'popup': False,
                'url': 'https://www.cau.ac.kr/',
                'x': 640,
                'y': 470,
            },
            {
                'name': 'Test',
                'popup': False,
                'url': 'https://www.cau.ac.kr/',
                'x': 1035,
                'y': 610,
            },
            {
                'name': 'Test',
                'popup': False,
                'url': 'https://www.cau.ac.kr/',
                'x': 500,
                'y': 700,
            },
            {
                'name': 'Test',
                'popup': False,
                'url': 'https://www.cau.ac.kr/',
                'x': 775,
                'y': 720,
            },
        ],
    }
    return HttpResponse(template.render(context, request))
