from django.urls import path
from escolaappweb_dashboard import views
from escolaappweb_dashboard import form_views

app_name = 'escolaappweb_dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('criar-turma/',views.create_turma_form, name='create-turma'),
    path('criar-materia/',views.create_materia_form, name='create-materia'),
    path('criar-pai/',views.create_pai_form, name='create-pai'),
    path('criar-aluno/',views.create_aluno_form, name='create-aluno'),
]
