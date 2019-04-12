from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy

from .models import ObitosHospitais


class ObitosHospitaisView(LoginRequiredMixin, ListView):
    context_object_name = "obitos_hospitais"
    queryset = ObitosHospitais.objects.all()
    template_name = "hospitais/lista_obitos_hospitais.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Óbitos em Hospitais'
        return context


class HospitaisView(LoginRequiredMixin, ListView):
    context_object_name = "hospitais"
    queryset = ObitosHospitais.objects.all()
    template_name = "hospitais/hospitais_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Hospitais'
        return context




"""
class CopaView(LoginRequiredMixin, ListView):
    context_object_name = "ordem_servicos"
    queryset = OrdemServico.objects.all()
    template_name = "ordem_servico/listagem_copa.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Copa'
        return context

"""
class ObitoHospitalCreate(LoginRequiredMixin, CreateView):
    model = ObitosHospitais
    fields = (
        'data_falecimento', 'hospital', 'funeraria', 'nome_falecido', 'nome_responsavel','tel_responsavel', 'motivo_nao_atendimento',
        'nome_atendente','nome_agente'
    )
    template_name = "hospitais/obito_hospitais_cadastro.html"
    success_url = reverse_lazy('hospitais:obitos_hospitais_listagem')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Lançar Óbito em Hospital Conveniado'
        return context






