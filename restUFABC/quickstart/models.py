from __future__ import unicode_literals

from django.db import models


class Turma(models.Model):
    name = models.CharField(max_length=80)
    turma = models.CharField(max_length=200)
    turma = models.CharField(max_length=200)
    turno = models.CharField(max_length=200)
    campus = models.CharField(max_length=200)
    disciplina = models.CharField(max_length=200)
    horarioteoria = models.CharField(max_length=20)
    horariopratica = models.CharField(max_length=20)
    professor = models.CharField(max_length=200)


    def __unicode__(self):
        return self.name

class AlunoLista(models.Model):
    name = models.CharField(max_length=80)
    curso = models.CharField(max_length=200)
    turmas = models.ManyToManyField(Turma, blank=True, )
    ra = models.IntegerField()

    def __unicode__(self):
        return self.name


class AlunoNotas(models.Model):
    name = models.CharField(max_length=80)
    curso = models.CharField(max_length=200)
    disciplina = models.CharField(max_length=200)
    nota = models.CharField(max_length=20)
    idcelular = models.IntegerField()

    def __unicode__(self):
        return self.name