from django.db import models
from django_stuff.models import TimestampedModel

# Create your models here.

SIGLA = (
    ('caixa','Cx'),
    ('unidade','Un'),
    ('fardo','Fd'),
    ('pacote','Pct')
)


class Medida(TimestampedModel):
    descricao = models.CharField(max_length = 15)
    sigla = models.CharField(max_length=22, default='unidade', choices=SIGLA)
    def __str__(self):
        return self.descricao
    



class Produtos(TimestampedModel):
    descricao = models.CharField(max_length=40)
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao
    