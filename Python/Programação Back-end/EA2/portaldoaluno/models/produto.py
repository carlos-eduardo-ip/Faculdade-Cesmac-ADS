from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=250, unique=True)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    validade = models.DateField(null=False)

    def __str__(self):
        return self.nome
