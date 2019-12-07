from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import RegistroHoraExtra
from django.urls import reverse_lazy

class RegistroHoraExtraView():
    model = RegistroHoraExtra
    fields = ('motivo','funcionario','horas')

class RegistroHoraExtraList(RegistroHoraExtraView, ListView):
    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa)

class RegistroHoraExtraNovo(RegistroHoraExtraView, CreateView):
    pass    

class RegistroHoraExtraEdit(RegistroHoraExtraView, UpdateView):
    pass    

class RegistroHoraExtraDelete(RegistroHoraExtraView, DeleteView):    
    success_url = reverse_lazy('list_registros_hora_extra')