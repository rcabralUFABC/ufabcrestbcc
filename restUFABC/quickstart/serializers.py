from django.contrib.auth.models import User, Group
from rest_framework import serializers
from restUFABC.quickstart.models import AlunoLista, Turma, AlunoNotas

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#   class Meta:
#        model = User
#        fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Group
#        fields = ('url', 'name')


# class BankSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Bank
#        fields = ('name', 'code')


class TurmaSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
        model = Turma
        fields = ('name', 'turma', 'turma', 'turno', 'campus', 'disciplina',
                  'horarioteoria', 'horariopratica', 'professor')


class AlunosListaSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
        model = AlunoLista
        fields = ('name', 'curso', 'turmas', 'ra')


class AlunoNotasSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
        model = AlunoNotas
        fields = ('name', 'curso', 'disciplina', 'nota', 'idcelular')


