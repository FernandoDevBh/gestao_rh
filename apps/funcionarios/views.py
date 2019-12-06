from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from functools import reduce
from django.contrib.auth.models import User
from .models import Funcionario
from django.urls import reverse_lazy

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ('nome', 'departamentos')

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ('nome', 'departamentos')

    def form_valid(self, form): 
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = reduce(lambda x, y: x+y ,funcionario.nome.split(' '))
        funcionario.user = User.objects.create_user(username=username)
        funcionario.save()
        return super().form_valid(form)