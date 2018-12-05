from django import forms
from escolaappweb_dashboard.models import Turma, Pai, Aluno, Materia
from escolaappweb_dashboard.constants import REGEX_TELEFONE

# CRUD Alunos, Pais, Turmas, Matérias

class PaiForm(forms.Form):
    # TODO: telefone Precisa ser validado com regex.
    # portanto, não é possivel utilizar ModelForm (?)
    nome = forms.CharField(label='Insira o nome')
    telefone = forms.RegexField(REGEX_TELEFONE
        # 99 99999 9999
        # 99 9999 9999
        # 99 99999-9999
        # 99 9999-9999
        # (99) 99999 9999
        # (99) 9999 9999
        # (99) 99999-9999
        # (99) 9999-9999
    )
    
    class Meta:
        model = Pai
        fields = [
            'nome',
            'telefone',
        ]

    def clean(self, *args, **kw):
        nome = self.cleaned_data('nome')
        telefone = self.cleaned_data('telefone')

        if any(char.isdigit() for char in nome):
            raise forms.ValidationError('Caractere inválido.')

        return super(PaiForm, self).clean(*args,**kw)


class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
