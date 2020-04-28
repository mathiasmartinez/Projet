from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Project, Task, Journal
from .forms import ConnexionForm,JournalForm,TaskForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur

                return redirect('projets', ident=user.id)
            else:  # sinon une erreur sera affichée
                error = True
        else:
            form = ConnexionForm()

    return render(request, 'taskmanager/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


def Listeprojects(request, ident):
    projects = Project.objects.filter(id=ident)
    return render(request, 'taskmanager/projects.html', locals())


def projet(request, ident):
    tasks = Task.objects.filter(id=ident)
    return render(request, 'taskmanager/project.html', locals())


def tache(request,ide):

    show = False
    task = Task.objects.get(id=ide)
    journal = Journal.objects.filter(id=ide)
    form = JournalForm(request.POST or None)
    if form.is_valid():
        show = form.cleaned_data['show']

    return render(request, 'taskmanager/tache.html', locals())

def newtask(request):
    taskform = TaskForm(request.POST or None)
    new = True
    if taskform.is_valid():
        new = False
        task = Task()
        task.project = taskform.cleaned_data['project']
        task.name = taskform.cleaned_data['name']
        task.description = taskform.cleaned_data['description']
        task.assignee = taskform.cleaned_data['assignee']
        task.start_date = taskform.cleaned_data['start_date']
        task.priority = taskform.cleaned_data['priority']
        task.status = taskform.cleaned_data['status']
        task.due_date = taskform.cleaned_data['due_date']
        task.save()
        return redirect('task',ide = task.id)
    return render(request,'taskmanager/newtask.html',locals())





