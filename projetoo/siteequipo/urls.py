from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('elenco/', views.elenco, name='elenco'),
    path('sobre/', views.sobre, name='sobre'),
]
