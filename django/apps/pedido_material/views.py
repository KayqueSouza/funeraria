from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy
from . import forms
from .models import PedidoMaterial
from .forms import PedidoMaterialForm, PedidoMaterialFormset


class PedidoMaterialView(LoginRequiredMixin, ListView):
    context_object_name = "pedidos_materiais"
    queryset = PedidoMaterial.objects.all()
    template_name = "pedido_material/listagem.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Pedidos de Materiais'
        return context



class PedidoMaterialCreate(LoginRequiredMixin, FormView):
    form_class = PedidoMaterialForm
    template_name = "pedido_material/pedido_material_cadastro.html"
    success_message = "<b>Orçamento de compra  </b>adicionado com sucesso."
    success_url = reverse_lazy('core:inicial')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Pedir Material'
        if self.request.POST:
            context['produto_set'] = PedidoMaterialFormset(self.request.POST, prefix='pedido_produto')
        else:
            context['produto_set'] = PedidoMaterialFormset(prefix='pedido_produto')
        return context

    def form_valid(self, form):
        pedido_material = form.save(commit=False)
        pedido_material.save()
        formsets = PedidoMaterialFormset(self.request.POST, prefix='pedido_produto')
        if formsets.is_valid():
            for formset in formsets:
                pedido_material_produto = formset.save(commit=False)
                pedido_material_produto.pedido_material = pedido_material
                pedido_material_produto.save()
        else:
            print(formsets.errors)
            return super().form_invalid(form)

        return super().form_valid(form)


    


"""
    def form_valid(self, form):
        context = self.get_context_data()
        produtos = context['produtos']
        with transaction.atomic():
            self.object = form.save()

            if produtos.is_valid():
                produtos.instance = self.object
                produtos.save()
        return super(PedidoMaterialCreate, self).form_valid(form)



"""
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