from django.urls import path
from . import views

app_name = 'ordem_servico'
urlpatterns = [
    path('', views.OrdemServicoView.as_view(), name='listagem'),
    path('/copa', views.CopaView.as_view(), name='listagem_copa'),
    path('/agentes', views.AgentesView.as_view(), name='agentes'),
    path('/os-create', views.OrdemServicoCreate.as_view(), name='os_create'),
]
