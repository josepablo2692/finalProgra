from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Presentacion, Producto, Categoria, Precio, Categorias
from .forms import PresentacionForm, CategoriaForm, ProductoForm
from django.http import HttpResponseRedirect


def Inicio(request):
    return render(request, 'blog/listar_productos.html', {})

def Listar_productos(request):
    productos = Producto.objects.order_by('nombre')
    return render(request, 'blog/listar_productos.html', {'productos': productos})

def Nueva_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.save()
            return redirect('blog.views.Detalle_categoria', pk=nuevo.pk)
    else:
        form = CategoriaForm()
    return render(request, 'blog/editar_categoria.html', {'categoria': form})

def Editar_categoria(request, pk):
    post = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.Detalle_categoria', pk=post.pk)
    else:
        form = CategoriaForm(instance=post)
    return render(request, 'blog/editar_categoria.html', {'categoria': form})

def Eliminar_categoria(request, pk):
    elimnar = get_object_or_404(Categoria, pk=pk)
    elimnar.delete()
    redirect('blog.views.Eliminar_categoria')
    return HttpResponseRedirect('/listar_categorias')

def Detalle_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'blog/detalle_categoria.html', {'categoria': categoria})

def Listar_categorias(request):
    categorias = Categoria.objects.order_by('nombre')
    return render(request, 'blog/listar_categorias.html', {'categorias': categorias})

def Nueva_presentacion(request):
    if request.method == "POST":
        form = PresentacionForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.save()
            return redirect('blog.views.Detalle_presentacion', pk=nuevo.pk)
    else:
        form = PresentacionForm()
    return render(request, 'blog/editar_presentacion.html', {'presentacion': form})

def Editar_presentacion(request, pk):
    post = get_object_or_404(Presentacion, pk=pk)
    if request.method == "POST":
        form = PresentacionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.Detalle_presentacion', pk=post.pk)
    else:
        form = PresentacionForm(instance=post)
    return render(request, 'blog/editar_presentacion.html', {'presentacion': form})

def Eliminar_presentacion(request, pk):
    elimnar = get_object_or_404(Categoria, pk=pk)
    elimnar.delete()
    redirect('blog.views.Eliminar_presentacion')
    return HttpResponseRedirect('/Listar_presentaciones')

def Detalle_presentacion(request, pk):
    presentacion = get_object_or_404(Presentacion, pk=pk)
    return render(request, 'blog/detalle_presentacion.html', {'presentacion': presentacion})

def Listar_presentaciones(request):
    presentaciones = Presentacion.objects.order_by('nombre')
    return render(request, 'blog/listar_presentaciones.html', {'presentaciones': presentaciones})

def Nuevo_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.save()
            return redirect('blog.views.Detalle_producto', pk=nuevo.pk)
    else:
        form = ProductoForm()
    return render(request, 'blog/editar_producto.html', {'producto': form})

def Editar_producto(request, pk):
    post = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.Detalle_producto', pk=post.pk)
    else:
        form = ProductoForm(instance=post)
    return render(request, 'blog/editar_producto.html', {'producto': form})

def Eliminar_producto(request, pk):
    elimnar = get_object_or_404(Producto, pk=pk)
    elimnar.delete()
    redirect('blog.views.Eliminar_producto')
    return HttpResponseRedirect('/Listar_productos')

def Detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    precios = Precio.objects.filter(producto=producto)
    categorias = Categorias.objects.filter(producto=producto)
    return render(request, 'blog/detalle_producto.html', {'producto': producto, 'precios':precios, 'categorias':categorias})

def Listar_productos(request):
    productos = Producto.objects.order_by('nombre')
    return render(request, 'blog/listar_productos.html', {'productos': productos})

#def Detalle_articulo(request, pk):
#    producto = get_object_or_404(Postear, pk=pk)
#    return render(request, 'blog/Detalle_producto.html', {'producto': producto})


#def categoria_nueva(request):
#    if request.method == "POST":
#        formulario = PeliculaForm(request.POST)
#        if formulario.is_valid():
#            pelicula = Pelicula.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
#            for actor_id in request.POST.getlist('actores'):
#                actuacion = Actuacion(actor_id=actor_id, pelicula_id = pelicula.id)
#                actuacion.save()
#            messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
#    else:
#        formulario = PeliculaForm()
#    return render(request, 'blog/pelicula_editar.html', {'formulario': formulario})
