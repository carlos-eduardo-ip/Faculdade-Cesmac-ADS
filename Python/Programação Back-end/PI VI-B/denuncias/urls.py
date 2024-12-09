from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import DenunciarView, TodosOsCasosView, CasosEmAbertoView, CasosFechadosView, CasosDetailView

app_name = 'denuncias'

urlpatterns = [
    path('', TemplateView.as_view(template_name='denuncias/pages/home.html'), name='home'),

    path('login/', auth_views.LoginView.as_view(template_name='denuncias/pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('denunciar/', DenunciarView.as_view(), name='denunciar'),
    path('denuncia/<int:pk>', CasosDetailView.as_view(), name='denuncia_detail'),
    path('todos-os-casos/', TodosOsCasosView.as_view(), name='todos_os_casos'),
    path('casos-em-aberto/', CasosEmAbertoView.as_view(), name='casos_em_aberto'),
    path('casos-fechados/', CasosFechadosView.as_view(), name='casos_fechados'),
]
