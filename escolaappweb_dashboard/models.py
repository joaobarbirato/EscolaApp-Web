from django.db import models

# Create your models here.

def get_all(model=None):
    return model.objects.all()

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


def get_all_by_key(key=None):
    if key == 'turma':
        return Turma.objects.all()
    elif key == 'materia':
        return Materia.objects.all()
    elif key == 'pai':
        return Pai.objects.all()
    elif key == 'aluno':
        return Aluno.objects.all()

def get_model_by_key(key=None):
    if key == 'turma':
        return Turma
    elif key == 'materia':
        return Materia
    elif key == 'pai':
        return Pai
    elif key == 'aluno':
        return Aluno
