from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Dashboard'
        return context


class InicialView(LoginRequiredMixin, TemplateView):
    template_name = "core/inicial.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Inicial'
        context['usuario'] = self.get_login_url()
        return context
