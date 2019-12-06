from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import RegistroHoraExtra
from django.urls import reverse_lazy

class RegistroHoraExtra():
    model = RegistroHoraExtra
    fields = ('motivo','funcionario',)

class RegistroHoraExtraList(RegistroHoraExtra, ListView):
    pass

class RegistroHoraExtraNovo(RegistroHoraExtra, CreateView):
    pass    

class RegistroHoraExtraEdit(RegistroHoraExtra, UpdateView):
    pass    

class RegistroHoraExtraDelete(RegistroHoraExtra, DeleteView):    
    success_url = reverse_lazy('list_registros_hora_extra')