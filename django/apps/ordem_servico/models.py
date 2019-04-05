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




class TipoServico(TimestampedModel):
    tipo_servico = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo_servico


class TaxaPagar(TimestampedModel):
    taxa = models.CharField(max_length=15)

    def __str__(self):
        return self.taxa


class LocalRemocao(TimestampedModel):
    local = models.CharField(max_length=40)

    def __str__(self):
        return self.local


class Preparacao(TimestampedModel):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Ornamentacao(TimestampedModel):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome


class Funeraria(TimestampedModel):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=30)
    fun_razao_social = models.CharField(max_length=50)
    fun_endereco = models.CharField(max_length=50)
    def __str__(self):
        return self.fun_razao_social


class TipoCafe(TimestampedModel):
    cafe = models.CharField(max_length=50)

    def __str__(self):
        return self.cafe


class OrdemServico(TimestampedModel):
    funeraria = models.ForeignKey(Funeraria, on_delete=models.CASCADE)
    falecido = models.CharField(max_length=50)
    cpf_falecido = models.CharField(max_length=50)
    especie = models.CharField(max_length=14, default='convencional', choices=TIPO_SERVICO)
    abrangencia = models.CharField(max_length=22, default='servico_completo', choices=ABRANGENCIA)
    tipo = models.ForeignKey(TipoServico, on_delete=models.CASCADE)
    taxas_apagar = models.ForeignKey(TaxaPagar, on_delete=models.CASCADE)
    remocao = models.ForeignKey(LocalRemocao, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    urna = models.IntegerField()
    biblia = models.BooleanField()
    cristo = models.BooleanField()
    sem_adereco = models.BooleanField()
    veu = models.BooleanField()
    preparacao = models.ForeignKey(Preparacao, on_delete=models.CASCADE)
    ornamentacao = models.ForeignKey(Ornamentacao, on_delete=models.CASCADE)
    obs_ornamentacao = models.CharField(max_length=50)
    cafe = models.ForeignKey(TipoCafe, on_delete=models.CASCADE)
    local_velorio = models.CharField(max_length=100, blank=True, null=True)
    local_sepultamento = models.CharField(max_length=100, blank=True, null=True)
    previsao_velorio = models.DateTimeField(blank=True, null=True)
    data_sepultamento = models.DateTimeField(blank=True, null=True)
    inicio_remocao = models.DateTimeField(blank=True, null=True)
    termino_remocao = models.DateTimeField(blank=True, null=True)
    inicio_urna = models.DateTimeField(blank=True, null=True)
    termino_urna = models.DateTimeField(blank=True, null=True)
    inicio_ctp = models.DateTimeField(blank=True, null=True)
    termino_ctp = models.DateTimeField(blank=True, null=True)
    inicio_cto = models.DateTimeField(blank=True, null=True)
    termino_cto = models.DateTimeField(blank=True, null=True)
    inicio_exp = models.DateTimeField(blank=True, null=True)
    termino_exp = models.DateTimeField(blank=True, null=True)
    inicio_cafe = models.DateTimeField(blank=True, null=True)
    termino_cafe = models.DateTimeField(blank=True, null=True)
    inicio_flora = models.DateTimeField(blank=True, null=True)
    termino_flora = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=22, default='aberto', choices=STATUS)

    def __str__(self):
        return self.falecido
