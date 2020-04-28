from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.connexion),
    path('deconnexion/', views.deconnexion),
    path('projects/<str:ident>/', views.Listeprojects), # Affichage de tous les projets d'un utilisateur
    path('connexion/<str:ident>/', views.Listeprojects, name='projets'), # Affichage de tous les projets d'un utilisateur
    path('project/<int:ident>/', views.projet, name='detail_project'), # Affichage des tâches d'un projet
    path('task/<int:ide>/',views.tache,name='task'), # Affichage des attributs d'une tâche
    path('newtask/',views.newtask, name='newtask'), # Création d'une nouvelle tâche
    path('edittask/<int:ide>/',views.edittask,name='edittask'), # Modification d'une tâche

]



