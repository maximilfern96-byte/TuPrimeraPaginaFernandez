from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria

def inicio(request):
    return render(request, 'blog/inicio.html')

def listado_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(titulo__icontains=query)
    else:
        posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts, 'query': query})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'blog/lista_categorias.html', {'categorias': categorias})

def posts_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    return render(request, 'blog/lista_posts.html', {'categoria': categoria, 'posts': posts})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': post})
