from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('nuevo/', views.crear_post, name='crear_post'),
    path('autor/nuevo/', views.crear_autor, name='crear_autor'),
    path('categoria/nuevo/', views.crear_categoria, name='crear_categoria'),
]
