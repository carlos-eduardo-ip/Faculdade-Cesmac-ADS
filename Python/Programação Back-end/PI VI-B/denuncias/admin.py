from django.contrib import admin
from .models import Denuncia

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'data_criacao', 'denunciante', 'anonimo']
    fields = ['titulo', 'status','descricao', 'denunciante', 'grupo', 'anonimo']

