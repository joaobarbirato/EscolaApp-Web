from django.db import models

# Create your models here.

"""
    @modelo: Turma
    @atr:
        - nome: Nome da turma (ex. turma1)
        - ano: Ano da turma (ex. 2o ano)
"""
class Turma(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    ano = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['nome']
        verbose_name = u'Turma'
        verbose_name_plural = u'Turmas'
    
    def __self__(self):
        return self.nome

    def __str__(self):
        return self.nome


"""
    @modelo: Materia
    @atr:
        - nome: Nome da matéria (ex. matemática)
"""
class Materia(models.Model):
    nome = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['nome']
        verbose_name = u'Matéria'
        verbose_name_plural = u'Matérias'

    def __self__(self):
        return self.nome

    def __str__(self):
        return self.nome


"""
    @modelo: Pai
    @atr:
        - nome: Nome do pai (ex. José)
        - telefone: Número de telefone - posteriormente será utilizado no aplicativo
            (ex. 99 99999 9999)
"""
class Pai(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    telefone = models.CharField(max_length=20, blank=False, default='00000000000000000000')
    
    class Meta:
        ordering = ['nome']
        verbose_name = u'Pai'
        verbose_name_plural = u'Pais'

    def __self__(self):
        return self.nome

    def __str__(self):
        return self.nome


"""
    @modelo: Aluno
    @atr:
        - nome: Nome do(a) aluno(a) (ex. Joãozinho)
        - turma (Chave Estrangeira p/ modelo Turma):
            turma a qual o(a) aluno(a) pertence
        - pai (Chave Estrangeira p/ modelo Pai):
            pai do(a) aluno(a)
"""
class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, blank=True)
    pai = models.ForeignKey(Pai, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = u'Aluno(a)'
        verbose_name_plural = u'Alunos(as)'

    def __self__(self):
        return self.nome

    def __str__(self):
        return self.nome

""" 
    get_all_by_key
    Retorna todos os objetos de um determinado modelo
    @key: parametro identificador de modelos
"""
def get_all_by_key(key=None):
    if key == 'turma':
        return Turma.objects.all()
    elif key == 'materia':
        return Materia.objects.all()
    elif key == 'pai':
        return Pai.objects.all()
    elif key == 'aluno':
        return Aluno.objects.all()

# Funções auxiliares

""" 
    get_all
    Retorna todos os objetos de um determinado modelo 
    @model: modelo que os objetos são.
"""
def get_all(model=None):
    return model.objects.all()

""" 
    get_model_by_key
    Retorna uma referência ao modelo especificado
    @key: parametro identificador de modelos
"""
def get_model_by_key(key=None):
    if key == 'turma':
        return Turma
    elif key == 'materia':
        return Materia
    elif key == 'pai':
        return Pai
    elif key == 'aluno':
        return Aluno
