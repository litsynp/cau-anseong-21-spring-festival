from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('festival/index.html')
    context = {
        'contents': [
            {
                'name': 'Test YouTube Link that pops up',
                'popup': True,
                'url': 'https://www.youtube.com/embed/TNsSBhl_2LI',
            },
            {
                'name': 'Test YouTube Link 2 on current tab',
                'popup': False,
                'url': 'https://www.youtube.com/embed/TNsSBhl_2LI',
            },
        ],
    }
    return HttpResponse(template.render(context, request))
