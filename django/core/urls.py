from django.urls import path
from core import views

app_name = 'core'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('operacional/', views.operacional, name='operacional'),
    path('copa/', views.copa, name='copa_copa'),
]
