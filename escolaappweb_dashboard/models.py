from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    turma = models.ForeignKey('Turma', on_delete=models.SET_NULL, null=True, blank=True)
    pai = models.ForeignKey('Pai', on_delete=models.SET_NULL, null=True, blank=True)

    def __self__(self):
        return self.nome

    def __str__(self):
        return self.nome


class Pai(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    telefone = models.CharField(max_length=20, blank=False, default='00000000000000000000')

    def __self__(self):
        return self.nome

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    ano = models.CharField(max_length=100, blank=False)

    def __self__(self):
        return self.nome

    def __str__(self):
        return self.nome


class Materia(models.Model):
    nome = models.CharField(max_length=100, blank=False)

    def __self__(self):
        return self.nome

    def __str__(self):
        return self.nome
