from django.contrib import admin
from .models import Cliente
from .models import Ingeniero
from .models import Proyecto
from .models import Actividad
from .models import Bitacora

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Ingeniero)
admin.site.register(Proyecto)
admin.site.register(Actividad)
admin.site.register(Bitacora)

# Register your models here.
