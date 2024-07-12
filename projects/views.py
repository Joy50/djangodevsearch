from django.shortcuts import render, redirect
from .models import Project, Review, Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def projects(request):
    projectsList = Project.objects.all()
    context ={'projects': projectsList}
    return render(request,'projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = Tag.objects.all()
    return render(request,'single-projects.html',{'project':projectObj})

@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'project-form.html',context)

@login_required(login_url="login")
def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance = project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance = project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'project-form.html',context)

@login_required(login_url="login")
def deleteObject(request,pk):
    project = Project.objects.get(id=pk)
    if(request.method == "POST"):
        project.delete()
        return redirect('projects')
    context = {'project':project}
    return render(request,'delete-template.html',context)