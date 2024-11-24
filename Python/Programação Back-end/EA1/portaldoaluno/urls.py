from django.urls import path
from . import views

app_name = 'portaldoaluno'

urlpatterns = [
    path('', views.home, name='home'),
    path('alunos/', views.listar_alunos, name='listar_alunos'),
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('create_aluno/', views.create_aluno, name='create_aluno'),
    path('create_curso/', views.create_curso, name='create_curso'),

    path('api/alunos/', views.AlunoAPIView.as_view(), name='api_alunos'),
    path('api/aluno/<int:pk>', views.AlunoAPIView.as_view(), name='api_aluno'),
    path('api/cursos/', views.CursoAPIView.as_view(), name='api_cursos'),
]
