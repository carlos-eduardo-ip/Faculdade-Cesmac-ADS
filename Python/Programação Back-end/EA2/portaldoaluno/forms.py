from django import forms
from .models import Produto

class CreateProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'validade']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
