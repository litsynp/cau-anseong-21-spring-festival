from django.urls import path

from . import views

app_name = 'festival'

urlpatterns = [
    path('', views.index, name='index'),
    # path('cau-image/', views.cau_image_page, name='cau_image_page'),
    path('escape-room/', views.escape_room, name='escape_room'),
    path('finding-puang/', views.finding_puang, name='finding_puang'),
    path('humanright-test/', views.humanright_test, name='humanright_test'),
    path('mixmusic-quiz/', views.mixmusic_quiz, name='mixmusic_quiz'),
    path('photo-puzzle/', views.photo_puzzle, name='photo_puzzle'),
    path('trickywords/', views.trickywords, name='trickywords'),
    path('whereareyou-chungang/', views.whereareyou_chungang,
         name='whereareyou_chungang'),
]
