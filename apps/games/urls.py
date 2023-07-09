from django.urls import path

# Local
from .views import index, about, get_game, video_games


urlpatterns = [
    path('', index),
    path('vgames/', video_games),
    path('about/', about),
    path('vgames/<int:game_id>/', get_game),
]
