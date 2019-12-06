from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import RegistroHoraExtra
from django.urls import reverse_lazy


class RegistroHoraExtraList(ListView):
    model = RegistroHoraExtra

class RegistroHoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    fields = ('motivo','funcionario',)

class RegistroHoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = ('motivo','funcionario',)

class RegistroHoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_registros_hora_extra')