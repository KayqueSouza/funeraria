from django.urls import path
from . import views

app_name = 'ordem_servico'
urlpatterns = [
    path('', views.OrdemServicoView.as_view(), name='listagem'),
]
