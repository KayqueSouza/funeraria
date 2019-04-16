from django.db import models
from django_stuff.models import TimestampedModel

# Create your models here.

SIGLA = (
    ('caixa','Cx'),
    ('unidade','Un'),
    ('fardo','Fd'),
    ('pacote','Pct')
)



ESTADOS = (
            ( "AC", "Acre" ),
            ( "AL", "Alagoas" ),
            ( "AP", "Amapá" ),
            ( "AM", "Amazonas" ),
            ( "BA", "Bahia" ),
            ( "CE", "Ceará" ),
            ( "DF", "Distrito Federal" ),
            ( "ES", "Espírito Santo" ),
            ( "GO", "Goiás" ),
            ( "MA", "Maranhão" ),
            ( "MT", "Mato Grosso" ),
            ( "MS", "Mato Grosso do Sul" ),
            ( "MG", "Minas Gerais" ),
            ( "PA", "Pará" ),
            ( "PB", "Paraíba" ),
            ( "PR", "Paraná" ),
            ( "PE", "Pernambuco" ),
            ( "PI", "Piauí" ),
            ( "RJ", "Rio de Janeiro" ),
            ( "RN", "Rio Grande do Norte" ),
            ( "RS", "Rio Grande do Sul" ),
            ( "RO", "Rondônia" ),
            ( "RR", "Roraima" ),
            ( "SC", "Santa Catarina" ),
            ( "SP", "São Paulo" ),
            ( "SE", "Sergipe" ),
            ( "TO", "Tocantins" )
)



class TipoHospital(TimestampedModel):
    tipo = models.CharField(max_length=15)
    def __str__(self):
        return self.tipo




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


class Hospitais(TimestampedModel):
    tipo = models.ForeignKey(TipoHospital, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, choices=ESTADOS, blank=True, null=True)
    site = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nome



class FunerariasMercado(TimestampedModel):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, choices=ESTADOS, blank=True, null=True)
    site = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nome
    