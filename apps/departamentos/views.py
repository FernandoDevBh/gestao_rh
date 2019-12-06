from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Departamento
from django.urls import reverse_lazy

class DepartamentoView():
    model = Departamento
    fields = ('nome',)

    def get_empresa(self):
        return self.request.user.funcionario.empresa

class DepartamentoList(DepartamentoView, ListView):
    
    def get_queryset(self):
        empresa = self.get_empresa()
        return Departamento.objects.filter(empresa=empresa)

class DepartamentoNovo(DepartamentoView, CreateView):

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.get_empresa()
        departamento.save()
        return super().form_valid(form)

class DepartamentoEdit(DepartamentoView, UpdateView):
    pass

class DepartamentoDelete(DepartamentoView, DeleteView):    
    success_url = reverse_lazy('list_departamentos')