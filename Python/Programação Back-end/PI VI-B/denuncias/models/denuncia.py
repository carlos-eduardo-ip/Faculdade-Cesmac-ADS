from django.db import models
from django.contrib.auth.models import User

class Denuncia(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    denunciante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    anonimo = models.BooleanField(default=False)
    grupo = models.CharField(max_length=50, null=True, blank=True, choices=[(None, "Nenhum"), ("SI", "Segurança da Informação")])
    agente_si = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="denuncias_atribuidas")
    status = models.CharField(max_length=20, choices=[("Aberto", "Aberto"), ("Em Tratamento", "Em Tratamento"), ("Fechado", "Fechado")], default="Aberto")
    comentarios = models.TextField(blank=True, null=True)

    def adicionar_comentario(self, autor, conteudo):
        from datetime import datetime
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        novo_comentario = f"{autor} - {data_hora}\n{conteudo}\n\n"
        self.comentarios = (self.comentarios or "") + novo_comentario
        self.save()

    def __str__(self) -> str:
        return self.titulo
