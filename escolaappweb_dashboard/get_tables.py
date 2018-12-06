from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from escolaappweb_dashboard.models import (
    Turma,
    Materia,
    Pai,
    Aluno,
    get_all
)

# __queryset_to_jsondict
# formata uma queryset para um dicionario a ser mandado como json
# @queryset: queryset
def __queryset_to_jsondict(queryset):
    dict_all = {}
    for i in range(queryset.count()):
        dict_all[str(queryset[i].id)] = queryset.values()[i]
    return dict_all

@login_required
def get_tabela_turma(request):
    all_objects = get_all(Turma)
    response = JsonResponse(__queryset_to_jsondict(all_objects))
    response.status_code = 200
    return response
    
@login_required
def get_tabela_materia(request):
    all_objects = get_all(Materia)
    response = JsonResponse(__queryset_to_jsondict(all_objects))
    response.status_code = 200
    return response
    
@login_required
def get_tabela_pai(request):
    all_objects = get_all(Pai)
    response = JsonResponse(__queryset_to_jsondict(all_objects))
    response.status_code = 200
    return response
    
@login_required
def get_tabela_aluno(request):
    all_objects = get_all(Aluno)
    response = JsonResponse(__queryset_to_jsondict(all_objects))
    response.status_code = 200
    return response
    
