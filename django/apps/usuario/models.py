from django.db import models

# Create your models here.

ESTADO_CIVIL = (
('solteiro','Solteiro(a)'),
('casado','Casado(a)'),
('divorciado','Divorciado(a)'),
('viuvo', 'Viúvo(a)')
)

class Usuario(models.Model):
    usuario_nome = models.CharField(max_length=100)
    usuario_cpf = models.CharField(max_length=14)
    usuario_rg = models.CharField(max_length=30)
    usuario_cep = models.CharField(max_length=11)
    usuario_profissao = models.CharField(max_length = 20)
    usuario_estado_civil = models.CharField(max_length = 20, choices=ESTADO_CIVIL)
    usuario_rua = models.CharField(max_length=50)
    usuario_bairro = models.CharField(max_length=20)
    usuario_cidade = models.CharField(max_length=20)
    usuario_email = models.EmailField()
    usuario_telefone = models.CharField(max_length=20)
    usuario_celular = models.CharField(max_length = 20)
    usuario_site = models.CharField(max_length = 30)

    

    def __str__(self):
        return  self.usuario_nome



