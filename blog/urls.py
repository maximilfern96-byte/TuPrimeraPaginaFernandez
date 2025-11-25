from django.urls import path
from .views import (
    inicio,
    listado_posts,
    lista_categorias,
    posts_por_categoria,
    detalle_post,
    crear_post,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('posts/', listado_posts, name='lista_posts'),
    path('categorias/', lista_categorias, name='lista_categorias'),
    path('categoria/<int:categoria_id>/', posts_por_categoria, name='posts_por_categoria'),
    path('post/<int:pk>/', detalle_post, name='detalle_post'),

    # Nueva ruta para crear posts
    path('crear/', crear_post, name='crear_post'),
]
