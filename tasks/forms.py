
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.forms import ModelForm
from .models import Cliente
from .models import Ingeniero
from .models import Proyecto
from .models import Actividad
from .models import Bitacora

from django import forms



class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['Tipo_ID', 'NID', 'Razon_social', 'Direccion', 'Email', 'Telefono']
        widgets = {
            'Tipo_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digita el tipo de ID'}),
            'NID': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digita el numero de identificacion'}),
            'Razon_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digita la razon social de la empresa'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digita la direccion de la empresa'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digita el e-mail de contacto empresarial'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digita el numero telefonico de contacto'}),
        }
        
class IngenieroForm(forms.ModelForm):
    class Meta:
        model = Ingeniero
        fields = ['COD_ingeniero', 'Identificacion', 'Nombres', 'Apellidos', 'Direccion','ROL', 'Telefono', 'Email']
        widgets = {
            'COD_ingeniero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el codigo del Ingeniero'}),
            'Identificacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el numero de identificacion'}),
            'Nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite los nombres'}),
            'Apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite los apellidos'}),
            'ROL': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite el ROL del ingeniero'}),
            'Email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite la direccion e-mail'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite la direccion de residencia'}),
            'Telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el numero de telefono'}),
            
        }

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['Codigo', 'Nombre', 'Descripcion', 'Costo']
        widgets = {
            'Codigo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el codigo del Proyecto'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite el nombre del proyecto'}),
            'Descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'De una descripcion del proyecto'}),
            'Costo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el costo del proyecto'}),
        }

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['COD_actividad', 'Nombre', 'Descripcion', 'Costo']
        widgets = {
            'COD_actividad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el codigo de la actividad'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite el nombre del proyecto'}),
            'Descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'De una descripcion del proyecto'}),
            'Costo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el costo del proyecto'}),
        }

        
class BitacoraForm(forms.ModelForm):
    class Meta:
        
       
        model = Bitacora
        exclude = ['COD_bitacora']
        fields = '__all__'
        widgets = {
            'Fecha': forms.DateInput(attrs={'type': 'date'}),
            'COD_bitacora': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el codigo de la Bitacora','readonly': 'readonly'}),
            'Numero_de_fuentes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite el numero de fuentes correspondiente a la anterior seleccion'}),
            'Indique_los_fuentes_trabajados': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Si su opcion es diferente a las desplegables indique el o los fuentes '}),
            'Nota': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite aquí si tiene alguna novedad'}),
        }

    