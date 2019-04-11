from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy

from .models import PedidoMaterial


class PedidoMaterialView(LoginRequiredMixin, ListView):
    context_object_name = "pedidos_materiais"
    queryset = PedidoMaterial.objects.all()
    template_name = "pedido_material/listagem.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Pedidos de Materiais'
        return context



class PedidoMaterialCreate(LoginRequiredMixin, CreateView):
    model = PedidoMaterial
    fields = (
        'funeraria', 'solicitante', 'produto', 'quantidade'
    )
    template_name = "pedido_material/pedido_material_cadastro.html"
    success_url = reverse_lazy('core:inicial')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Pedir Material'
        return context



"""
class OrdemServicoView(LoginRequiredMixin, ListView):
    context_object_name = "ordem_servicos"
    queryset = OrdemServico.objects.all()
    template_name = "ordem_servico/listagem.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ordem de Serviço'
        return context
"""