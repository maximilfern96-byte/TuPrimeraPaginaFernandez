from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Categoria
from .forms import PostForm

# -------------------------------------------------------
#                  📌 INICIO
# -------------------------------------------------------

def inicio(request):
    return render(request, 'inicio.html')


# -------------------------------------------------------
#                  📌 LISTADO DE POSTS
# -------------------------------------------------------

def listado_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(titulo__icontains=query)
    else:
        posts = Post.objects.all()

    return render(request, 'lista_posts.html', {
        'posts': posts,
        'query': query
    })


# -------------------------------------------------------
#                  📌 LISTA DE CATEGORÍAS
# -------------------------------------------------------

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {
        'categorias': categorias
    })


# -------------------------------------------------------
#                  📌 POSTS POR CATEGORÍA
# -------------------------------------------------------

def posts_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)

    return render(request, 'lista_posts.html', {
        'categoria': categoria,
        'posts': posts
    })


# -------------------------------------------------------
#                  📌 DETALLE DEL POST
# -------------------------------------------------------

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detalle_post.html', {
        'post': post
    })


# -------------------------------------------------------
#                  📌 CREAR POST
# -------------------------------------------------------

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "El post se creó correctamente.")
            return redirect("lista_posts")
    else:
        form = PostForm()

    return render(request, "crear_post.html", {
        "form": form
    })
