from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, 'blog/base.html')

def lista_posts(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        posts = Post.objects.filter(titulo__icontains=busqueda)
    else:
        posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'blog/form_post.html', {'form': form})
from .forms import AutorForm, CategoriaForm  # <-- sumar estas importaciones

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_post')  # después de crear autor, voy a crear post
    else:
        form = AutorForm()
    return render(request, 'blog/form_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_post')
    else:
        form = CategoriaForm()
    return render(request, 'blog/form_categoria.html', {'form': form})
