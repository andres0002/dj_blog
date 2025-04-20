# django
from django.urls import path
# third
# own
from apps.blog.views import (
    home_view, generals_view, programation_view, video_games_view, tecnology_view, detail_post_view,
    HomeView, GeneralsView, ProgramationView, VideoGamesView, TecnologyView, DetailPostView
)

urlpatterns = [
    # function
    # path('', home_view, name='index'),
    # path('general/', generals_view, name='general'),
    # path('programation/', programation_view, name='programation'),
    # path('videogames/', video_games_view, name='videogames'),
    # path('tecnology/', tecnology_view, name='tecnology'),
    # path('<slug:slug>', detail_post_view, name='detail_post'),
    # class
    path('', HomeView.as_view(), name='index'),
    path('general/', GeneralsView.as_view(), name='general'),
    path('programation/', ProgramationView.as_view(), name='programation'),
    path('videogames/', VideoGamesView.as_view(), name='videogames'),
    path('tecnology/', TecnologyView.as_view(), name='tecnology'),
    path('<slug:slug>', DetailPostView.as_view(), name='detail_post'),
]