from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('dashboard', views.HomeView.as_view(), name='home'),
    path('', views.InicialView.as_view(), name = 'inicial')
    
]
