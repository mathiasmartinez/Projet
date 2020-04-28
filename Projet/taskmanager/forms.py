from django import forms
from .models import Task

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class JournalForm(forms.Form):
    show = forms.BooleanField(help_text="Show history",required=False)

class TaskForm(forms.ModelForm):
    class Meta :
        model = Task
        fields = '__all__'

