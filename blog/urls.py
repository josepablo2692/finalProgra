from django.conf.urls import url
from django.conf import settings
from . import views


#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva
# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.
urlpatterns = [
    url(r'^$', views.Listar_productos),
    url(r'^listar_categorias/$', views.Listar_categorias, name='Categorias'),
    url(r'^categoria/(?P<pk>[0-9]+)/editar/$', views.Editar_categoria, name='editar_categoria'),
    url(r'^categoria/(?P<pk>[0-9]+)/detalle/$', views.Detalle_categoria, name='detalle_categoria'),
    url(r'^categoria/(?P<pk>[0-9]+)/eliminar/$', views.Eliminar_categoria, name='eliminar_categoria'),
    url(r'^categoria/nueva/$', views.Nueva_categoria, name='Nueva_categoria'),

    url(r'^listar_presentaciones/$', views.Listar_presentaciones, name='Presentaciones'),
    url(r'^presentacion/(?P<pk>[0-9]+)/editar/$', views.Editar_presentacion, name='editar_presentacion'),
    url(r'^presentacion/(?P<pk>[0-9]+)/detalle/$', views.Detalle_presentacion, name='detalle_presentacion'),
    url(r'^presentacion/(?P<pk>[0-9]+)/eliminar/$', views.Eliminar_presentacion, name='eliminar_presentacion'),
    url(r'^presentacion/nueva/$', views.Nueva_presentacion, name='Nueva_presentacion'),

    url(r'^listar_productos/$', views.Listar_productos, name='Productos'),
    url(r'^producto/(?P<pk>[0-9]+)/editar/$', views.Editar_producto, name='editar_producto'),
    url(r'^producto/(?P<pk>[0-9]+)/detalle/$', views.Detalle_producto, name='detalle_producto'),
    url(r'^producto/(?P<pk>[0-9]+)/eliminar/$', views.Eliminar_producto, name='eliminar_producto'),
    url(r'^producto/nuevo/$', views.Nuevo_producto, name='Nuevo_producto'),

    #url(r'^post/(?P<pk>[0-9]+)/editar_categoria/$', views.Editar_categoria, name='Editar_categoria'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    #url(r'^post/new/$', views.nuevo_producto, name='nuevo_articulo'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar_articulo, name='editar_articulo'),
    ]
