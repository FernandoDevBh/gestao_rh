from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from apps.funcionarios.models import Funcionario
from .serializers import FuncionarioSerializer

class  FuncionarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]