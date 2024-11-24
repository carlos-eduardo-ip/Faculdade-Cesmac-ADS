from django import forms
from .models import Aluno, Curso

class CreateAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'email']

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CreateCursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descricao']

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'