from django.contrib import admin
from api.models import Local,Dueno,Mascota,Cita,Servicio

# Register your models here.

admin.site.register(Local)
admin.site.register(Dueno)
admin.site.register(Mascota)
admin.site.register(Servicio)
admin.site.register(Cita)