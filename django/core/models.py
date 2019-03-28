from django.db import models
import math
import datetime





class Especies(models.Model):
    especies = models.CharField(max_length = 30)
    def __str__(self):
        return self.especies

class Abrangencia(models.Model):
    abrangencia = models.CharField(max_length = 30)
    def __str__(self):
        return self.abrangencia

class TipoServico(models.Model):
    tipo_servico = models.CharField(max_length = 30)
    def __str__(self):
        return self.tipo_servico

class TaxasPagar(models.Model):
    taxas_pagar = models.CharField(max_length=15)
    def __str__(self):
        return self.taxas_pagar


class LocalRemocao(models.Model):
    local_remocao = models.CharField(max_length=40)
    def __str__(self):
        return self.local_remocao

class Preparacao(models.Model):
    preparacao = models.CharField(max_length=50)
    def __str__(self):
        return self.preparacao

class Ornamentacao(models.Model):
    ornamentacao = models.CharField(max_length=40)
    def __str__(self):
        return self.ornamentacao


class Funerarias(models.Model):
    funeraria = models.CharField(max_length = 50)
    cnpj = models.CharField(max_length = 30)
    def __str__(self):
        return self.funeraria

class Cafe(models.Model):
    cafe = models.CharField(max_length = 50)
    def __str__(self):
        return self.cafe

class Servico(models.Model):
    funeraria = models.ForeignKey(Funerarias, on_delete='')
    falecido = models.CharField(max_length=50)
    cpf_fal = models.CharField(max_length=50)
    especie = models.ForeignKey(Especies, on_delete='')
    abrangencia = models.ForeignKey(Abrangencia, on_delete='')
    tipo = models.ForeignKey(TipoServico, on_delete='')
    taxas_apagar = models.ForeignKey(TaxasPagar, on_delete='')
    remocao = models.ForeignKey(LocalRemocao, on_delete='')
    os = models.IntegerField()
    urna = models.IntegerField()
    biblia = models.BooleanField()
    Cristo = models.BooleanField()
    sem_adereco = models.BooleanField()
    veu = models.BooleanField()
    preparacao = models.ForeignKey(Preparacao, on_delete='')
    ornamentacao = models.ForeignKey(Ornamentacao, on_delete='')
    obs_ornamentacao = models.CharField(max_length=50)
    cafe = models.ForeignKey(Cafe, on_delete='')
    local_vel = models.CharField(max_length=100, blank=True, null=True)
    local_sep = models.CharField(max_length=100, blank=True, null=True)
    prev_vel = models.DateTimeField(blank=True, null=True)
    data_sep = models.DateTimeField(blank=True, null=True)
    i_rem = models.DateTimeField(blank=True, null=True)
    t_rem = models.DateTimeField(blank=True, null=True)
    i_urna = models.DateTimeField(blank=True, null=True)
    t_urna = models.DateTimeField(blank=True, null=True)
    i_ctp = models.DateTimeField(blank=True, null=True)
    t_ctp = models.DateTimeField(blank=True, null=True)
    i_cto = models.DateTimeField(blank=True, null=True)
    t_cto = models.DateTimeField(blank=True, null=True)
    i_exp = models.DateTimeField(blank=True, null=True)
    t_exp = models.DateTimeField(blank=True, null=True)
    i_cafe = models.DateTimeField(blank=True, null=True)
    t_cafe = models.DateTimeField(blank=True, null=True)
    i_flora = models.DateTimeField(blank=True, null=True)
    t_flora = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.falecido



