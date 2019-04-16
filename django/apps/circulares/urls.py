from django.urls import path
from . import views

app_name = 'circulares'
urlpatterns = [
    path('', views.CircularesView.as_view(), name='circulares_list'),
    path('circular/', views.CircularView.as_view(), name='circular')        
]
