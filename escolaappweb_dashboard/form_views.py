from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from escolaappweb_dashboard.views import (
    __FORM,
    _get_index_context,
)

# __verify_form
# Retorna a devida resposta para um determinado modelo.
# @request: requisicao para view
# @key: chave para identificar qual form
def __verify_form(request,key=None):
    if key in __FORM:
        if request.method == 'POST':
            form = __FORM[key](request.POST)
            if form.is_valid():
                form.save()
                response = JsonResponse({"success":"form valido"})
                response.status_code = 200
                return response
            else:
                response = JsonResponse({"error":form.as_ul()})
                response.status_code = 550
                return response
        else:
            return render(request,'400.html',{})
            
    return render(request,'404.html',{})
    
# Views específicas para cada modelo

## post criação de Turma
@login_required
def post_turma_form(request):
    return __verify_form(request=request, key='turma')

## post criação de Materia
@login_required
def post_materia_form(request):
    return __verify_form(request=request, key='materia')

## post criação de Pai
@login_required
def post_pai_form(request):
    return __verify_form(request=request, key='pai')
    
## post criação de Aluno
@login_required
def post_aluno_form(request):
    return __verify_form(request=request, key='aluno')
    