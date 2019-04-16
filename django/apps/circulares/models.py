from django.db import models
from django_stuff.models import TimestampedModel
from apps.usuario.models import Usuario
from apps.core.models import Setor



class Circular(TimestampedModel):
    emitente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    setor_destinatario = models.ForeignKey(Setor, on_delete=models.CASCADE)
    data_criacao = models.DateField()
    assunto = models.CharField(max_length = 200) 
    texto = models.CharField(max_length = 500)
    
    def __str__(self):
        return self.emitente.__str__()
