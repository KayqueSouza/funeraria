from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView, DetailView, TemplateView
from django.urls import reverse_lazy

from .models import PAD


class PADView(LoginRequiredMixin, TemplateView):
    pass



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