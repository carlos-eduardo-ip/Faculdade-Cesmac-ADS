from django import forms
from .models import Denuncia
from django.contrib.auth.models import User

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['titulo', 'descricao', 'anonimo']

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['anonimo'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})

class CoordenadorForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['grupo', 'agente_si']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['agente_si'].queryset = User.objects.filter(groups__name="Agentes de SI")
        self.fields['grupo'].widget.attrs['class'] = 'form-control'
        self.fields['agente_si'].widget.attrs['class'] = 'form-control'
