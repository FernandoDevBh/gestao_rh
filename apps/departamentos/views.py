from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Departamento
from django.urls import reverse_lazy


class DepartamentoList(ListView):
    model = Departamento

class DepartamentoNovo(CreateView):
    model = Departamento
    fields = ('nome',)

class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ('nome',)

class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')