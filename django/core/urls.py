from django.urls import path, include
from .views import (home, operacional, copa)

urlpatterns = [
    
    path('operacional/', operacional, name = 'operacional'),
    path('copa/', copa, name='copa_copa'),
    path('', home, name='core_home')


]