from django.urls import path
from . import views

app_name = 'portaldoaluno'

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('create/', views.create_produtos, name='create'),

    path('api/produtos/', views.ProdutoAPIView.as_view(), name='api_produtos'),
    path('api/produto/<int:pk>/', views.ProdutoDetailAPIView.as_view(), name='api_produto'),
]
