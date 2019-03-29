from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import OrdemServico


class OrdemServicoView(LoginRequiredMixin, TemplateView):
    template_name = "ordem_servico/listagem.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ordem_servicos = OrdemServico.objects.all()
        context['page_title'] = 'Ordem de Serviço'
        context['ordem_servicos'] = ordem_servicos
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
