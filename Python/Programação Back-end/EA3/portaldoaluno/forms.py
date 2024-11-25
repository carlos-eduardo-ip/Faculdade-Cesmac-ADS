from django import forms
from .models import Usuario

class CreateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email']

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
