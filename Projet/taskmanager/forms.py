from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class JournalForm(forms.Form):
    show = forms.BooleanField(help_text="Show history",required=False)