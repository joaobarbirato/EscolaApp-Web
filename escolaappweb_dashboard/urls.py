efrom django.urls import path
from escolaappweb_dashboard import views

app_name = 'escolaappweb_dashboard'

urlpatterns = [
    path('', views.index, name='index'),
]
