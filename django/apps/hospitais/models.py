from django.db import models
from django_stuff.models import TimestampedModel
from apps.core.models import Hospitais, FunerariasMercado
from apps.usuario.models import Usuario

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

MOTIVOS = (
    ('plano','Já possui plano'),
    ('concorrencia','Optou por outra empresa'),
    ('gratuidade','Gratuidade'),
    ('motivo_nao_informado','Motivo não informado')
)




class ObitosHospitais(TimestampedModel):
    data_falecimento = models.DateField()
    hospital = models.ForeignKey(Hospitais, on_delete=models.CASCADE)
    funeraria = models.ForeignKey(FunerariasMercado, on_delete=models.CASCADE)
    nome_falecido = models.CharField(max_length = 100)
    nome_responsavel = models.CharField(max_length = 100)
    tel_responsavel = models.CharField(max_length = 30)
    motivo_nao_atendimento = models.CharField(max_length = 50, default= 'motivo_nao_informado', choices=MOTIVOS)
    nome_atendente = models.CharField(max_length = 100)
    nome_agente = models.ForeignKey(Usuario, on_delete=models.CASCADE)



    def __str__(self):
        return self.nome_falecido