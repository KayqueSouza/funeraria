from django.urls import path
from . import views

app_name = 'pedido_material'
urlpatterns = [
    path('', views.PedidoMaterialView.as_view(), name='listagem'),
    path('novo/', views.PedidoMaterialCreate.as_view(), name='criar'),
]
