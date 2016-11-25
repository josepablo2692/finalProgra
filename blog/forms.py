from django import forms
from .models import Presentacion, Producto, Categoria

class PresentacionForm(forms.ModelForm):
    class Meta:
        model = Presentacion
        fields = ('nombre',)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'foto', 'precentaciones', 'categoriast',)

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.

def __init__ (self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["precentaciones"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["precentaciones"].help_text = "Ingrese las presentaciones"
#En este caso le indicamos que nos muestre todos las presentaciones, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["precentaciones"].queryset = Presentacion.objects.all()

        self.fields["categoriast"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["categoriast"].help_text = "Ingrese las presentaciones"
        self.fields["categoriast"].queryset = Presentacion.objects.all()
