from django.shortcuts import render
from .models import Project

# Create your views here.


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


def detail(request, pk):
    project_detail = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project_detail': project_detail})
