from django.db import models
from django_stuff.models import TimestampedModel
from apps.ordem_servico.models import Funeraria
from apps.usuario.models import Usuario
from apps.core.models import Produtos





STATUS = (
    ('aberto', 'Aberto'),
    ('cotando', 'Em Cotação'),
    ('disponivel', 'Disponível para retirada'),
    ('finalizado','Finalizado'),
    ('naoatendido', 'Não atendido')
)





class PedidoMaterial(TimestampedModel):
    funeraria = models.ForeignKey(Funeraria, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    data_cotando = models.DateTimeField(blank=True, null=True)
    data_disponivel = models.DateTimeField(blank=True, null=True)
    data_finalizado = models.DateTimeField(blank=True, null=True)
    status_atual = models.CharField(max_length=22, default='aberto', choices=STATUS)

    def __str__(self):
        return self.solicitante.__str__()


class PedidoMaterialProduto(models.Model):
    pedido_material = models.ForeignKey(
        PedidoMaterial, related_name='produtos', on_delete=models.CASCADE,
    )
    produto = models.ForeignKey(
        Produtos, related_name='pedidos', on_delete=models.CASCADE,
    )
    quantidade = models.IntegerField(default=0)
    

    def _str_(self):
        return '{}: {}'.format(self.produto, self.quantidade)