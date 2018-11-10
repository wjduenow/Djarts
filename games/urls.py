from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rules$', views.rules, name='rules'),
    url(r'^new_game$', views.new_game, name='new_game'),
    url(r'^start_game$', views.start_game, name='start_game'),
    url(r'^game_type/([0-9]*)$', views.game_type, name='game_type'),
    url(r'^game/([0-9]*)$', views.game, name='game'),
    url(r'^games$', views.games, name='games'),
    url(r'^players$', views.players, name='players'),
]


