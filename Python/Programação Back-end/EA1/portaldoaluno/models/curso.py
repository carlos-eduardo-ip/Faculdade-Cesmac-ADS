from django.db import models
from .aluno import Aluno

class Curso(models.Model):
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    alunos = models.ManyToManyField(Aluno, related_name="cursos")

    def __str__(self):
        return self.titulo
