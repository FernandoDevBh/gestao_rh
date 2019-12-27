from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from apps.registro_hora_extra.models import RegistroHoraExtra
from .serializers import RegistroHoraExtraSerializer

class  RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    