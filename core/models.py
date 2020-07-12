from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) # cria campo de no max 100 caracteres
    descricao = models.TextField(blank=True, null=True)
    data_event  = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao  = models.DateTimeField(auto_now=True) # auto_now insere a hora atual
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # Define que o nome da tabela seja evento
    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_event.strftime('%d/%m/%Y %H:%MHrs')
    def get_data_input_evento(self):
        return self.data_event.strftime('%Y-%m-%dT%H:%M')
    def get_evento_atrasado(self):
        if self.data_event < datetime.now():
            return True
        else:
            return False