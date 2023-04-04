from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
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

numeroFuentes = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),   
    (5, 'Otro valor')
]

state = [
    (1, 'Seleccione'),
    (2, 'En proceso'),
    (3, 'Terminado')
]
type_font = [
    (1, 'Seleccione'),
    (2, 'RPG'),
    (3, 'RPGLE'),
    (3, 'RPGLE y RPG'),
    (3, 'Otro'),
]

workedFonts = [
    (1, 'Seleccione'),
    (2, 'RPG'),
    (3, 'RPGLE'),
]

class Bitacora(models.Model):
    Fecha = models.DateField()
    COD_bitacora = models.AutoField(primary_key=True)
    Horas_laboradas = models.FloatField(max_length=5, null=False)
    Proyecto= models.ForeignKey(Proyecto, null=True,  on_delete=models.CASCADE)
    Actividad= models.ForeignKey(Actividad, null=True,  on_delete=models.CASCADE)
    Cantidad_de_fuentes_trabajados = models.IntegerField(
        null=False, blank=False,
        choices=numeroFuentes,
        default=1
    )
    Numero_de_fuentes = models.IntegerField(null=True, blank=True, max_length=2)
    Tipos_de_fuentes_trabajados = models.IntegerField(
        null=False, blank=False,
        choices=type_font,
        default=1
    )
    Indique_los_fuentes_trabajados = models.CharField(null=True, blank=True, max_length=50)
    Estado_de_los_fuentes_trabajados = models.IntegerField(
        null=False, blank=False,
        choices=state,
        default=1
    )
    
    Nota = models.TextField(max_length=300, null=True, blank=True,) 
    
    
    
   
