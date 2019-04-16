from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.site.site_header = 'Sistema Metropax Admin'
admin.site.site_title = 'Sistema Metropax'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('ordem_servico/', include('apps.ordem_servico.urls')),
    path('pedido_material/', include('apps.pedido_material.urls')),
    path('hospitais/', include('apps.hospitais.urls')),
    path('circulares/', include('apps.circulares.urls')),


]
