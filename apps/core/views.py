from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps.funcionarios.models import Funcionario
from .serializers import UserSerializer, GroupSerializer
from .tasks import send_relatorio

@login_required
def home(request):
    data = {'usuario':request.user }
    return render(request, 'core/index.html', data)

def celery(request):
    send_relatorio.delay()
    return HttpResponse('Tarefa incluída na fila para execução.')

class  UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer