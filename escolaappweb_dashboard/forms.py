from django import forms
from escolaappweb_dashboard.models import Turma, Pai, Aluno, Materia
from escolaappweb_dashboard.constants import REGEX_TELEFONE

# Formulários de Criação de Alunos, Pais, Turmas, Matérias

"""
    TurmaForm
    Formulário de criação do modelo Turma
"""
class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'

"""
    MateriaForm
    Formulário de criação do modelo Matéria
"""
class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'


from re import compile as verifica_com_regex

"""
    PaiForm
    Formulário de criação do modelo Pai
    @metodos:
        - clean: validação de campos
"""
class PaiForm(forms.ModelForm):
    class Meta:
        model = Pai
        fields = [
            'nome',
            'telefone',
        ]

    # validação de campos
    def clean(self, *args, **kw):
        nome = self.cleaned_data.get('nome')
        telefone = self.cleaned_data.get('telefone')
        if any(char.isdigit() for char in nome):
            raise forms.ValidationError('Caractere inválido.')

        # Verifica se o telefone está no padrão estabelecido na máscara
        pattern = verifica_com_regex(REGEX_TELEFONE)
        print(pattern.match(telefone))
        if pattern.match(telefone) is None:
            raise forms.ValidationError('Formato de telefone inválido!')

        return super(PaiForm, self).clean(*args,**kw)


"""
    AlunoForm
    Formulário de criação do modelo Aluno
"""
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
