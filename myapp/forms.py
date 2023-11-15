from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Fecha de la cita", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description=forms.CharField(label="Nombre de la cita", widget=forms.Textarea(attrs={'class': 'input'}))
    

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del paciente", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))