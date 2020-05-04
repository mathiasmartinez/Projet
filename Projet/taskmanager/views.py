from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Project, Task, Journal,Status
from django.contrib.auth.models import User
from .forms import ConnexionForm,JournalForm,TaskForm,EditTaskForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def connexion(request):
    '''Page de connexion d'un utilisateur '''
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # On vérifie si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # on connecte l'utilisateur

                return redirect('projects', user=user.id)
            else:  # Sinon un message d'erreur sera affiché
                error = True
        else:
            form = ConnexionForm()

    return render(request, 'taskmanager/connexion.html', locals())



def deconnexion(request):
    '''Page de déconnexion d'un utilisateur'''
    logout(request)
    return redirect(reverse(connexion))


@login_required
def Listeprojects(request, user):
    '''Vue qui affiche la liste des projets d'un utilisateur'''
    projects = Project.objects.filter(members=user) #On récupère les projets de l'utilisateur connecté
    user_connected = User.objects.get(id=user) # On récupère l'utilisateur connecté pour afficher son nom
    if request.user == user_connected :
        return render(request, 'taskmanager/projects.html', locals())
    else:
        return render(request, 'taskmanager/ErreurAcces.html', {'user':user_connected})

def is_present(user,project):
    p = Project.objects.get(id=project)
    u = User.objects.get(id=user)
    mem = p.members.all()
    for m in mem :
        if m.id==u.id :
            return True
    return False

def projet(request, user, ident):
    ''' Vue qui affiche les tâches d'un projet'''
    projet = Project.objects.get(id=ident)
    if(is_present(user,ident)) :

        tasks = Task.objects.filter(project_id=ident) #On récupère les tâches de l'utilisateur concerné
        return render(request, 'taskmanager/project.html', locals())
    else :
        return render(request, 'taskmanager/ErreurAcces.html', locals())



def tache(request,ide):
    '''Vue qui affiche une tâche en particulier'''
    show = False # Par défaut, on n'affichera pas l'historique du journal
    #Récupération des données qui concernent la tâche concernée par l'identifiant ide
    task = Task.objects.get(id=ide)
    journal = Journal.objects.filter(task_id=ide)
    p = Project.objects.get(id=task.project_id)
    user = request.user
    if is_present(request.user.id,task.project.id):

        form = JournalForm(request.POST or None) # Création du formulaire vide ou avec les données déjà entrées
         # si l'utilisateur n'y accède pas pour la 1ère fois

        if form.is_valid():
            # On récupère le booléen stipulant si on doit afficher l'historique du journal
            show = form.cleaned_data['show']

        return render(request, 'taskmanager/tache.html', locals())
    else :
        return render(request,'taskmanager/ErreurAcces.html',locals())



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

    edittaskform = EditTaskForm(request.POST or None) # Création d'un formulaire
    # pour permetre à l'utilisateur de modifier une tâche

    # Récupération des données nécessaires à l'affichage du formulaire
    task =  Task.objects.get(id=ide)

    # Récupération des entrées actuelles des attributs de la tâche
    # afin de les afficher par défaut dans le formulaire
    current_project = Project.objects.get(id=task.project.id)
    current_status = Status.objects.get(name=task.status.name)
    current_user = User.objects.get(username=task.assignee.username)

    # Récupération des entrées de la base de données que l'utilisateur peut choisir
    # pour modifier la tâche.
    projects = Project.objects.exclude(id=task.project.id)
    status = Status.objects.exclude(name=task.status.name)
    users = User.objects.exclude(username=task.assignee.username)

    if edittaskform.is_valid():
        # On utilise la variable task pour modifier les entrées des attributs
        # de la tâche à modifier
        project_name = edittaskform.cleaned_data['project'] # Récupération du projet auquel est assigné la tâche dans le formulaire
        task.project = Project.objects.get(name=project_name)
        task.name = edittaskform.cleaned_data['name']
        task.description = edittaskform.cleaned_data['description']
        assignee = edittaskform.cleaned_data['assignee']
        task.assignee = User.objects.get(username=assignee)
        task.start_date = edittaskform.cleaned_data['start_date']
        task.priority = edittaskform.cleaned_data['priority']
        status_name = edittaskform.cleaned_data['status']
        task.status = Status.objects.get(name=status_name)
        task.due_date = edittaskform.cleaned_data['due_date']
        task.save() # On enregistre la tâche dans la base de données pour la modifier.
        return redirect('task',ide = task.id) # On renvoie l'utilisateur vers la page d'affichage de la tâche modifiée.

    return render(request, 'taskmanager/edittask.html', locals())
