from django.http import HttpResponse
from django.template import loader
from django.urls import reverse


def index(request):
    template = loader.get_template('festival/index.html')
    context = {
        'contents': [
            {
                'name': '방탈출',
                'popup': False,
                'url': reverse('festival:escape_room'),
                'x': 1025,
                'y': 180,
            },
            {
                'name': '푸앙이를 찾아라',
                'popup': False,
                'url': reverse('festival:finding_puang'),
                'x': 830,
                'y': 250,
            },
            {
                'name': '나의 교내 인권 상식 테스트',
                'popup': False,
                'url': reverse('festival:humanright_test'),
                'x': 1025,
                'y': 400,
            },
            {
                'name': '믹스음악퀴즈',
                'popup': False,
                'url': reverse('festival:mixmusic_quiz'),
                'x': 640,
                'y': 470,
            },
            {
                'name': '틀린그림찾기',
                'popup': False,
                'url': reverse('festival:photo_puzzle'),
                'x': 1035,
                'y': 610,
            },
            {
                'name': '말난장찾기',
                'popup': False,
                'url': reverse('festival:trickywords'),
                'x': 500,
                'y': 700,
            },
            {
                'name': '중앙아 어딨니?',
                'popup': False,
                'url': reverse('festival:whereareyou_chungang'),
                'x': 775,
                'y': 720,
            },
        ],
    }
    return HttpResponse(template.render(context, request))


def cau_image_page(request):
    template = loader.get_template('festival/cau_image_page.html')
    context = {}
    return HttpResponse(template.render(context, request))


def escape_room(request):
    """
    방탈출
    """
    template = loader.get_template('festival/escape_room.html')
    context = {}
    return HttpResponse(template.render(context, request))


def finding_puang(request):
    """
    푸앙이를 찾아라
    """
    template = loader.get_template('festival/finding_puang.html')
    context = {}
    return HttpResponse(template.render(context, request))


def humanright_test(request):
    """
    나의 교내 인권 상식 테스트
    """
    template = loader.get_template('festival/humanright_test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def mixmusic_quiz(request):
    """
    믹스음악퀴즈
    """
    template = loader.get_template('festival/mixmusic_quiz.html')
    context = {}
    return HttpResponse(template.render(context, request))


def photo_puzzle(request):
    """
    틀린그림찾기
    """
    template = loader.get_template('festival/photo_puzzle.html')
    context = {}
    return HttpResponse(template.render(context, request))


def trickywords(request):
    """
    말난장찾기
    """
    template = loader.get_template('festival/trickywords.html')
    context = {}
    return HttpResponse(template.render(context, request))


def whereareyou_chungang(request):
    """
    중앙아 어딨니?
    """
    template = loader.get_template('festival/whereareyou_chungang.html')
    context = {}
    return HttpResponse(template.render(context, request))
