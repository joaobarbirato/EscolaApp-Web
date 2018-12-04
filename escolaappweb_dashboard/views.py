from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(request=request, template_name="dashboard/index.html", context={})


def erro_400(request):
    return render(request=request, template_name="400.html", context={})


def erro_403(request):
    return render(request=request, template_name="400.html", context={})


def erro_404(request):
    return render(request=request, template_name="404.html", context={})


def erro_500(request):
    return render(request=request, template_name="500.html", context={})