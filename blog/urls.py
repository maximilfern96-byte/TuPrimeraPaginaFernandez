from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('listado/', views.listado_posts, name='listado'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categoria/<int:categoria_id>/', views.posts_por_categoria, name='posts_por_categoria'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
]
