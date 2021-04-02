from django.urls import path

from . import views

app_name = 'festival'

urlpatterns = [
    path('', views.index, name='index'),
    path('cau-image/', views.cau_image_page, name='cau_image_page'),
]
