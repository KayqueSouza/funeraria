from django.urls import path
from . import views

app_name = 'hospitais'
urlpatterns = [
    path('', views.HospitaisView.as_view(), name='hospitais_home'),
    path('obitos-hospitais/', views.ObitosHospitaisView.as_view(), name='obitos_hospitais_listagem'),
    path('novo/', views.ObitoHospitalCreate.as_view(), name='novo_obito_hospital'),
    
]
