from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy

from .models import OrdemServico


class OrdemServicoView(LoginRequiredMixin, ListView):
    context_object_name = "ordem_servicos"
    queryset = OrdemServico.objects.all()
    template_name = "ordem_servico/listagem.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ordem de Serviço'
        return context


class CopaView(LoginRequiredMixin, ListView):
    context_object_name = "ordem_servicos"
    queryset = OrdemServico.objects.all()
    template_name = "ordem_servico/listagem_copa.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Copa'
        return context


class OrdemServicoCreate(LoginRequiredMixin, CreateView):
    model = OrdemServico
    fields = (
        'funeraria', 'falecido', 'cpf_falecido', 'especie', 'abrangencia', 'tipo',
        'taxas_apagar', 'remocao', 'codigo', 'urna', 'biblia', 'cristo', 'sem_adereco',
        'veu', 'preparacao', 'ornamentacao', 'obs_ornamentacao', 'cafe', 'local_velorio',
        'local_sepultamento', 'previsao_velorio', 'data_sepultamento', 'inicio_remocao',
        'termino_remocao', 'inicio_urna', 'termino_urna', 'inicio_ctp', 'termino_ctp',
        'inicio_cto', 'termino_cto', 'inicio_exp', 'termino_exp', 'inicio_cafe', 'termino_cafe',
        'inicio_flora', 'termino_flora'
    )
    template_name = "ordem_servico/os_cadastro.html"
    success_url = reverse_lazy('ordem_servico:listagem')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Ordem de Serviço'
        return context


class AgentesView(LoginRequiredMixin, ListView):
    context_object_name = "ordem_servicos"
    queryset = OrdemServico.objects.all()
    template_name = "ordem_servico/agentes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Agentes'
        return context


def copa(request):
    servico = OrdemServico.objects.all()
    return render(request, 'ordem_servico/copa.html', {'servico': servico})


def copa_update(request, id):
    servico = OrdemServico.objects.get(id=2)
    tent = OrdemServico.objetos.filter(id=2).first()
    tent.falecido = tent.falecido + "alterado!"
    tent.save()
    print('passou por aqui')
    data = {'servico': servico, 'tent': tent}
    return render(request, 'ordem_servico//copa.html', data)
