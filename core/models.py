from django.db import models
from django.contrib.auth.models import User
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