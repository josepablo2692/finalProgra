#recuerde que es necesario indicar que clases de nuestro modelo van a ser manejadas por la aplicación /admin.
from django.contrib import admin
from blog.models import Presentacion, Producto, PresentacionAdmin, ProductoAdmin, Categoria, CategoriaAdmin

#Registramos nuestras clases principales.
admin.site.register(Presentacion, PresentacionAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
