from django.urls import path
from escolaappweb_dashboard import (
    views,
    form_views,
    get_api
)

app_name = 'escolaappweb_dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('criar-turma/',views.create_turma_form, name='create-turma'),
    path('criar-materia/',views.create_materia_form, name='create-materia'),
    path('criar-pai/',views.create_pai_form, name='create-pai'),
    path('criar-aluno/',views.create_aluno_form, name='create-aluno'),
]

# urls de POST
urlpatterns += [
    path('Z_DW0-DW5qQNuwp9hw9Oew/', form_views.post_turma_form, name='post-turma'),
    path('LZ8f19Zbu87FVtSHC58XBQ/', form_views.post_materia_form, name='post-materia'),
    path('jCj7tJ3kZqYb7Ha6t1Q-TQ/', form_views.post_pai_form, name='post-pai'),
    path('rClyYqAXQy7PQtWpamTkiA/', form_views.post_aluno_form, name='post-aluno'),
]

# urls de tabelas
urlpatterns += [
    path('tabela-turma/',views.table_turma_data, name='table-turma'),
    path('tabela-materia/',views.table_materia_data, name='table-materia'),
    path('tabela-pai/',views.table_pai_data, name='table-pai'),
    path('tabela-aluno/',views.table_aluno_data, name='table-aluno'),
]

# urls de API GET
urlpatterns += [
    path('8lcuAh9rhmnWpOWiqWxeZg/', get_api.get_json_turma, name='get-json-turma'),
    path('0OmOY5GQRB0f6-GZ-cc49w/', get_api.get_json_materia, name='get-json-materia'),
    path('M76OmD3dP_vbeaBHw6fLVQ/', get_api.get_json_pai, name='get-json-pai'),
    path('_TJjhAmN1ElAdqQGzaQGMg/', get_api.get_json_aluno, name='get-json-aluno'),
]
