from django.db import models
from django_stuff.models import TimestampedModel

ABRANGENCIA = (
    ('servico_completo', 'Servico Funerário Completo'),
    ('apenas_coroa_arranjos', 'Apenas Coroa e Arranjos')
)
TIPO_SERVICO = (
    ('convencional', 'Convencional'),
    ('falta_falecer', 'Falta Falecer'),
    ('iml', 'IML')
)
STATUS = (
    ('aberto', 'Aberto'),
    ('executando', 'Executando'),
    ('fechado', 'Fechado')
)




class PAD(models.Model):
    item = models.CharField(max_length = 10)