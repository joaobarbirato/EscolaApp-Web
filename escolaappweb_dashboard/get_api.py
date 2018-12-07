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
"""
    get_api
        Funções que retornam JSON com todos os dados de modelos específicos.
        As APIs serão úteis para a aplicação mobile.
"""
# __queryset_to_jsondict
# formata uma queryset para um dicionario a ser mandado como json
# @queryset: queryset
def __queryset_to_jsondict(queryset):
    dict_all = {}
    for i in range(queryset.count()):
        dict_all[str(queryset[i].id)] = queryset.values()[i]
    return dict_all

# get JSON

## modelo Turma
def get_json_turma(request):
    all_objects = get_all(Turma)
    response = JsonResponse(__queryset_to_jsondict(all_objects))
    response.status_code = 200
    return response
    
## modelo Materia
def get_json_materia(request):
    all_objects = get_all(Materia)
    response = JsonResponse(__queryset_to_jsondict(all_objects))
    response.status_code = 200
    return response
    
## modelo Pai
def get_json_pai(request):
    all_objects = get_all(Pai)
    response = JsonResponse(__queryset_to_jsondict(all_objects))
    response.status_code = 200
    return response

## modelo Aluno
def get_json_aluno(request):
    all_objects = get_all(Aluno)
    response = JsonResponse(__queryset_to_jsondict(all_objects))
    response.status_code = 200
    return response
    
