from django.contrib import admin
from core.models import Evento
# Register your models here.




class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','data_event','data_criacao')
    list_filter =  ('titulo','data_event',)

# registrar tabela criada no models
admin.site.register(Evento, EventoAdmin)