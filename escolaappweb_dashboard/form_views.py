from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def post_turma_forms(request):
    pass

@login_required
def post_materia_form(request):
    pass
    
@login_required
def post_aluno_form(request):
    pass

@login_required
def post_pai_form(request):
    pass
    