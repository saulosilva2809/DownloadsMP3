from django import forms
from .models import Musica

class AdicionarMusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['url', 'nome_arquivo']
