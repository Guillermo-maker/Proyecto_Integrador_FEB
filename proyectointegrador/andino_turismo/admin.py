from django.contrib import admin

from .models import Bus, Chofer,Atractivo, Parada, DetalleCadaParada, Recorrido, Viaje


# Register your models here.

admin.site.register(Bus)
admin.site.register(Chofer)
admin.site.register(Atractivo)
admin.site.register(Parada)
admin.site.register(DetalleCadaParada)
admin.site.register(Recorrido)
admin.site.register(Viaje)