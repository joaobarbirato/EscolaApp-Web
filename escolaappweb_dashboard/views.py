from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from escolaappweb_dashboard.forms import (
    TurmaForm,
    MateriaForm,
    PaiForm,
    AlunoForm
)
# Create your views here.

# Dicionario de forms
__FORM = {
    'turma': TurmaForm,
    'materia': MateriaForm,
    'pai': PaiForm,
    'aluno': AlunoForm,
}

# __get_create_context
# Retorna contexto padrao de view para formulario de create
# @key: chave para dicionario __FORM
def __get_create_context(key=None):
    contexto = {}
    if key in __FORM:
        contexto['form'] = __FORM[key]()
        contexto['model'] = __FORM[key].Meta.model._meta.verbose_name.title().lower()
    return contexto

# _get_index_context
# Retorna contexto padrao para index (importante para form_views)
def _get_index_context():
    return {}

# Tela de início
@login_required
def index(request):
    contexto = _get_index_context()
    return render(request=request, template_name="dashboard/index.html", context=contexto)

# Telas de acesso a formulários
## Create turma
@login_required
def create_turma_form(request):
    contexto = __get_create_context(key='turma')
    return render(request=request, template_name="dashboard/create.html", context=contexto)

## Create materia
@login_required
def create_materia_form(request):
    contexto = __get_create_context(key='materia')
    return render(request=request, template_name="dashboard/create.html", context=contexto)

## Create pai
@login_required
def create_pai_form(request):
    contexto = __get_create_context(key='pai')
    return render(request=request, template_name="dashboard/create.html", context=contexto)

## Create aluno
@login_required
def create_aluno_form(request):
    contexto = contexto = __get_create_context(key='aluno')
    return render(request=request, template_name="dashboard/create.html", context=contexto)

# Views para handlers de erro
def erro_400(request):
    return render(request=request, template_name="400.html", context={})


def erro_403(request):
    return render(request=request, template_name="400.html", context={})


def erro_404(request):
    return render(request=request, template_name="404.html", context={})


def erro_500(request):
    return render(request=request, template_name="500.html", context={})