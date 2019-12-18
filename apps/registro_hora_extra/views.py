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

class RegistroHoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({ 'user': self.request.user })
        return kwargs

class RegistroHoraExtraEdit(RegistroHoraExtraEditBase):
    def get_success_url(self):
        return reverse_lazy('update_registros_hora_extra', args=[self.object.id])

class RegistroHoraExtraEditFuncionario(RegistroHoraExtraEditBase):
    pass

class RegistroHoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_registros_hora_extra')