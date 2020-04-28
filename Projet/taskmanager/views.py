from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Project, Task, Journal,Status
from django.contrib.auth.models import User
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
            user = authenticate(username=username, password=password)  # On vérifie si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # on connecte l'utilisateur

                return redirect('projets', ident=user.id)
            else:  # Sinon un message d'erreur sera affiché
                error = True
        else:
            form = ConnexionForm()

    return render(request, 'taskmanager/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


def Listeprojects(request, ident):
    '''Vue qui affiche la liste des projets d'un utilisateur'''
    projects = Project.objects.filter(id=ident) #On récupère les projets de l'utilisateur connecté
    return render(request, 'taskmanager/projects.html', locals())


def projet(request, ident):
    ''' Vue qui affiche les tâches d'un projet'''
    projet = Project.objects.get(id=ident)
    tasks = Task.objects.filter(project_id=ident) #On récupère les tâches de l'utilisateur concerné
    return render(request, 'taskmanager/project.html', locals())


def tache(request,ide):
    '''Vue qui affiche une tâche en particulier'''
    show = False # Par défaut, on n'affichera pas l'historique du journal
    #Récupération des données qui concernent la tâche concernée par l'identifiant ide
    task = Task.objects.get(id=ide)
    journal = Journal.objects.filter(id=ide)
    form = JournalForm(request.POST or None) # Création du formulaire vide ou avec les données déjà entrées
    # si l'utilisateur n'y accède pas pour la 1ère fois

    if form.is_valid():
        # On récupère le booléen stipulant si on doit afficher l'historique du journal
        show = form.cleaned_data['show']

    return render(request, 'taskmanager/tache.html', locals())

def newtask(request):
    '''Vue qui affiche un formulaire de création d'une nuvelle tâche'''
    taskform = TaskForm(request.POST or None)

    if taskform.is_valid():

        task = Task() # Création d'un nouvel objet Task dans la base de donnée
        # Assignation de tous les paramètres récupérés dans le form
        task.project = taskform.cleaned_data['project']
        task.name = taskform.cleaned_data['name']
        task.description = taskform.cleaned_data['description']
        task.assignee = taskform.cleaned_data['assignee']
        task.start_date = taskform.cleaned_data['start_date']
        task.priority = taskform.cleaned_data['priority']
        task.status = taskform.cleaned_data['status']
        task.due_date = taskform.cleaned_data['due_date']
        task.save()
        return redirect('task',ide = task.id) # Redirection de l'utilisateur vers la page de la tâche concernée
        # en utilisant son identifiant
    return render(request,'taskmanager/newtask.html',locals())

def edittask(request,ide):

    taskform = TaskForm(request.POST or None)
    projects = Project.objects.all()
    task =  Task.objects.get(id=ide)
    status = Status.objects.all()
    users = User.objects.all()
    if taskform.is_valid():

        Task.objects.get(id=ide).project = taskform.cleaned_data['project']
        Task.objects.get(id=ide).name = taskform.cleaned_data['name']
        Task.objects.get(id=ide).description = taskform.cleaned_data['description']
        Task.objects.get(id=ide).assignee = taskform.cleaned_data['assignee']
        Task.objects.get(id=ide).start_date = taskform.cleaned_data['start_date']
        Task.objects.get(id=ide).priority = taskform.cleaned_data['priority']
        Task.objects.get(id=ide).status = taskform.cleaned_data['status']
        Task.objects.get(id=ide).due_date = taskform.cleaned_data['due_date']
        Task.objects.get(id=ide).save()
        return redirect('task',ide = task.id)
    return render(request, 'taskmanager/edittask.html', locals())






