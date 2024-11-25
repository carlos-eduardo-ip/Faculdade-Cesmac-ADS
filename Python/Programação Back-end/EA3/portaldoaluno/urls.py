from django.urls import path
from . import views

app_name = 'portaldoaluno'

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('create/', views.create_usuario, name='create'),

    path('api/produtos/', views.UsuarioAPIView.as_view(), name='api_usuarios'),
    path('api/produto/<int:pk>/', views.UsuarioDetailAPIView.as_view(), name='api_usuario'),
]
