from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from apps.empresas.models import Empresa


class EmpresaView():
    model = Empresa
    fields = ('nome', )

class EmpresaCreate(EmpresaView, CreateView):    

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('Ok')

class EmpresaEdit(EmpresaView, UpdateView):
    pass    