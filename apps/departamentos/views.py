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

class DepartamentoList(DepartamentoView, ListView):
    pass

class DepartamentoNovo(DepartamentoView, CreateView):
    pass

class DepartamentoEdit(DepartamentoView, UpdateView):
    pass

class DepartamentoDelete(DepartamentoView, DeleteView):    
    success_url = reverse_lazy('list_departamentos')