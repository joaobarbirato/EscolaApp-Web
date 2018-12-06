from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from escolaappweb_dashboard.views import (
    __FORM,
    _get_index_context,
    create_turma_form,
    create_materia_form,
    create_pai_form,
    create_aluno_form
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
                #TODO: tratar com JSON?
                response = JsonResponse({"success":"form valido"})
                response.status_code = 200
                print(form.errors)
                return response#render(request=request, template_name='dashboard/index.html', context=_get_index_context())
            else:
                #TODO: forms nao valido
                pass
        else:
            #TODO: render BAD REQUEST
            pass
    response = JsonResponse({"error":form.as_ul()})
    response.status_code = 550
    return response#render(request=request, template_name='dashboard/create.html', context={'form':form,'model':key})
    

@login_required
def post_turma_form(request):
    return __verify_form(request=request, key='turma')

@login_required
def post_materia_form(request):
    return __verify_form(request=request, key='materia')

@login_required
def post_pai_form(request):
    return __verify_form(request=request, key='pai')
    
@login_required
def post_aluno_form(request):
    return __verify_form(request=request, key='aluno')
    