from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Project, Task, Status
from .forms import ConnexionForm
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
    task = Task.objects.get(id=ide)
    return render(request, 'taskmanager/tache.html', locals())
