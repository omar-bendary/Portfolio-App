from django.shortcuts import render
from projects_app.models import Project


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


<<<<<<< HEAD
def win(request):
    pass
=======
def mac(request):
    pass
>>>>>>> c27a9093770a84e7533eccd507d737abc28b4177
