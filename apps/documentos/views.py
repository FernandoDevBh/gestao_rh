from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Documento
from django.urls import reverse_lazy

class DocumentoView():
    model = Documento
    fields = ('descricao','arquivo',)

class DocumentoList(DocumentoView, ListView):
    pass

class DocumentoNovo(DocumentoView, CreateView):
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']
        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)

class DocumentoEdit(DocumentoView, UpdateView):
    pass

class DocumentoDelete(DocumentoView, DeleteView):
    pass