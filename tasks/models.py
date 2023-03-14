from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Create your models here.
class Cliente(models.Model):
    Tipo_ID = models.CharField(max_length=10)
    NID = models.IntegerField(primary_key=True)
    Razon_social = models.CharField(max_length=70)
    Direccion = models.CharField(max_length=70)
    Email = models.CharField(max_length=70) 
    Telefono = models.IntegerField()
    
    
    def __str__(self):
        return self.Razon_social + '- by' + self.user.username
    
class Ingeniero(models.Model):
    COD_ingeniero = models.IntegerField(primary_key=True)
    Identificacion = models.IntegerField()
    Username = models.CharField(null=True, max_length=70)
    Nombres = models.CharField(max_length=70)
    Apellidos = models.CharField(max_length=70)
    ROL = models.CharField(max_length=50) 
    Direccion = models.CharField(max_length=80)
    Telefono = models.IntegerField()
    Email = models.CharField(max_length=70) 
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
class Proyecto(models.Model):
    Codigo = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=500)
    Costo = models.FloatField(max_length=(9,2))
    user = models.ForeignKey(User, null=True,  on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True,  on_delete=models.CASCADE)
    ingeniero = models.ForeignKey(Ingeniero, null=True, on_delete=models.CASCADE)
    
class Actividad(models.Model):
    COD_actividad = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=500)
    Costo = models.FloatField(max_length=(9,2))
    user = models.ForeignKey(User, null=True,  on_delete=models.CASCADE)
    proyecto= models.ForeignKey(Proyecto, null=True,  on_delete=models.CASCADE)
    ingeniero= models.ForeignKey(Ingeniero, null=True,  on_delete=models.CASCADE)

class Bitacora(models.Model):
    COD_bitacora = models.IntegerField(primary_key=True)
    Horas_laboradas = models.IntegerField()
    Fuentes_trabajados = models.CharField(max_length=70)
    Tipo_fuente = models.CharField(max_length=70)
    Descripcion = models.TextField(max_length=300) 
    Estado = models.CharField(max_length=30)
   



# Create your models here.
