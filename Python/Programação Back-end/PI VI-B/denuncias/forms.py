from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['titulo', 'descricao', 'anonimo']

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['anonimo'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
