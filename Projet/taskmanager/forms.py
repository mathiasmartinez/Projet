from django import forms
from .models import Task

class ConnexionForm(forms.Form):
    ''' Form de connexion d'un utilisateur'''
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class JournalForm(forms.Form):
    '''Form permettant de décider de l'affichage de l'historique du journal '''
    show = forms.BooleanField(help_text="Show history",required=False)

class TaskForm(forms.ModelForm):
    class Meta :
        model = Task # Form calqué sur la classe Task
        fields = '__all__' # On utilise tous les champs de la classe Task pour
        #  créer un nouvel objet de cette classe

class EditTaskForm(forms.Form):
    name = forms.CharField(required=False)
    project = forms.IntegerField(required=False)
    assignee = forms.CharField(required=False)
    start_date = forms.DateTimeField(required=False)
    due_date = forms.DateTimeField(required=False)
    priority = forms.IntegerField(required=False)
    status = forms.CharField(required=False)