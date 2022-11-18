from django.contrib import admin
from django.urls import path,  include
from .views import index_view, detalhes_view, header_view


urlpatterns = [
    path('', index_view, name='Home'),
    path('header', header_view, name='header'),
    path('<int:discos_id>', detalhes_view, name='Detalhes')
]
