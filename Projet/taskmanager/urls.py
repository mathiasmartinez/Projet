from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.connexion),
    path('deconnexion/',views.deconnexion),
    path('projects/',views.project),
    path('connexion/<str:nom>/',views.project),
]
