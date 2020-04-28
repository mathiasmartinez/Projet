from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.connexion),
    path('deconnexion/', views.deconnexion),
    path('projects/<str:ident>/', views.Listeprojects),
    path('connexion/<str:ident>/', views.Listeprojects, name='projets'),
    path('project/<int:ident>/', views.projet),
    path('task/<int:ide>/',views.tache,name='task'),
    path('newtask/',views.newtask),
    path('edittask/<int:ide>/',views.edittask),

]



