from django.db import models
from django.contrib import admin
from django.dispatch import receiver

class Presentacion(models.Model):
    nombre  =   models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='media/fotos/')
    precentaciones = models.ManyToManyField(Presentacion, through='Precio')
    categoriast = models.ManyToManyField(Categoria, through='Categorias')


    def __str__(self):
        return self.nombre

class Precio (models.Model):
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    preciomin = models.DecimalField(max_digits=6, decimal_places=2)
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Categorias (models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class PrecioInLine(admin.TabularInline):
    model = Precio
    extra = 1

class CategoriasInLine(admin.TabularInline):
    model = Categorias
    extra = 1

class ProductoAdmin (admin.ModelAdmin):
    inlines = (CategoriasInLine,PrecioInLine,)

class PresentacionAdmin(admin.ModelAdmin):
    inlines = (PrecioInLine,)

class CategoriaAdmin(admin.ModelAdmin):
    inlines = (CategoriasInLine,)
