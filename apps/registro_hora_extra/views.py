from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import RegistroHoraExtra
from django.urls import reverse_lazy
from .forms import RegistroHoraExtraForm


class RegistroHoraExtraList(ListView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa)

class RegistroHoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraNovo, self).get_form_kwargs()
        kwargs.update({ 'user': self.request.user })
        return kwargs

class RegistroHoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraEdit, self).get_form_kwargs()
        kwargs.update({ 'user': self.request.user })
        return kwargs

class RegistroHoraExtraDelete(DeleteView):    
    success_url = reverse_lazy('list_registros_hora_extra')