from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download/', views.baixar_musica, name='baixar_musica'),
]
