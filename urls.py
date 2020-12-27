from django.urls import path

from . import views

app_name = 'boardgames'
urlpatterns = [
    # path('<str:game_name>/', views.game_detail, name='detail'),
    path('', views.index_view, name='boardgames'),
]
