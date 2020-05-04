from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.connexion),#Affichage de la page de connexion
    path('deconnexion/', views.deconnexion, name='logout'),
    path('projects/<str:user>/', views.Listeprojects, name='projects'), # Affichage de tous les projets d'un utilisateur
    path('project/<str:user>/<int:ident>/', views.projet, name='detail_project'), # Affichage des tâches d'un projet
    path('task/<int:ide>/',views.tache,name='task'), # Affichage des attributs d'une tâche
    path('newtask/',views.newtask, name='newtask'), # Création d'une nouvelle tâche
    path('edittask/<int:ide>/',views.edittask,name='edittask'), # Modification d'une tâche

]



