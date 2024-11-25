from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField(max_length=500, null=False, unique=True)

    def __str__(self):
        return self.nome
