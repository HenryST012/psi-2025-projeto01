from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('elenco/', views.elenco, name='elenco'),
    path('sobre/', views.sobre, name='sobre'),
    path('blog/', views.blog_index, name='blog_index'),
    path('blog/post/<int:post_id>/', views.blog_post, name='blog_post'),
]