from django.views import View
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)

import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas

from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

from functools import reduce
from django.contrib.auth.models import User
from .models import Funcionario
from django.urls import reverse_lazy

def reportlab_view(request):
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachachment; filename="mypdf.pdf"'
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(10, 810, 'Relatório de Funcionários')

    base = 'Nome: %s | Hora Extra: %.2f |'

    y = 790

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    for f in funcionarios:
        p.drawString(10, y, base % (f.nome, f.total_horas_extra))
        y -= 40

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):
    def get(self, request, *args, **kwargs):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel Sales',
            'request': request,
        }

        return Render.render('funcionarios/relatorio.html', params, 'myfile')

class FuncionarioView():
    model = Funcionario
    fields = ('nome', 'departamentos')

class FuncionariosList(FuncionarioView, ListView):
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset

class FuncionarioEdit(FuncionarioView, UpdateView):
    pass

class FuncionarioDelete(FuncionarioView, DeleteView):    
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioNovo(FuncionarioView, CreateView):    

    def form_valid(self, form): 
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = reduce(lambda x, y: x+y ,funcionario.nome.split(' '))
        funcionario.user = User.objects.create_user(username=username)
        funcionario.save()
        return super().form_valid(form)