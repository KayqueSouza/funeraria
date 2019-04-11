from django.urls import path
from . import views

app_name = 'pad'
urlpatterns = [
    path('', views.PADView.as_view(), name='teste'),

]
