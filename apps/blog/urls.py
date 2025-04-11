# django
from django.urls import path
# third
# own
from apps.blog.views import home, generals, programation, video_games, tecnology, detail_post

urlpatterns = [
    path('', home, name='index'),
    path('general/', generals, name='general'),
    path('programation/', programation, name='programation'),
    path('videogames/', video_games, name='videogames'),
    path('tecnology', tecnology, name='tecnology'),
    path('<slug:slug>', detail_post, name='detailpost'),
]