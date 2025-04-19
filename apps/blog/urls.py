# django
from django.urls import path
# third
# own
from apps.blog.views import generals_view, programation_view, video_games_view, tecnology_view, detail_post_view

urlpatterns = [
    path('general/', generals_view, name='general_func'),
    path('programation/', programation_view, name='programation_func'),
    path('videogames/', video_games_view, name='videogames_func'),
    path('tecnology/', tecnology_view, name='tecnology_func'),
    path('<slug:slug>', detail_post_view, name='detail_post_func'),
]