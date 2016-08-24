from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from restUFABC.quickstart.serializers import AlunoNotasSerializer, AlunosListaSerializer, TurmaSerializer
from restUFABC.quickstart.models import AlunoNotas, AlunoLista, Turma

# class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = User.objects.all().order_by('-date_joined')
#    serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows groups to be viewed or edited.
#    """
#    queryset = Group.objects.all()
#    serializer_class = GroupSerializer


# class BanksViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows groups to be viewed or edited.
#    """
#    queryset = Bank.objects.all()
#    serializer_class = BankSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer


class AlunoNotasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = AlunoNotas.objects.all()
    serializer_class = AlunoNotasSerializer


class AlunoListaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = AlunoLista.objects.all()
    serializer_class = AlunosListaSerializer