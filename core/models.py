from django.db import models
import math
import datetime

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete='')
    placa = models.CharField(max_length=7)
    proprietario = models.ForeignKey(Pessoa, on_delete='')
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()
    def __str__(self):
        return self.marca.nome + ' - '+self.placa


class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5,decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return 'Parâmetros Gerais'


class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, blank=True, null=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete='')
    pago = models.BooleanField(default=False)

    def horas_total(self):
        return 2#math.ceil((self.checkout- self.checkin).total_seconds()/3600)

    def total(self):
        return self.valor_hora*self.horas_total()

    def __str__(self):
        return self.veiculo.placa 


class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo,on_delete='')
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.inicio)


class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista,on_delete='')
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6,decimal_places=2)
    def __str__(self):
        return str(self.mensalista) + ' - '+str(self.total)



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

class Alimentacao(models.Model):
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



