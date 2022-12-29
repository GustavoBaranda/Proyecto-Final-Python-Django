from django.forms import ModelForm
from django import forms
from .models import Tasks

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'important']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),
            'important' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
            # 'datecompleted' : forms.SelectDateWidget(attrs={'class' : 'date form-control'})
        }
        labels = {
            'title': 'Titulo:',
            'description' : 'Descripcion:',
            'important' : 'Importate ',
            # 'datecompleted' : 'Tarea completada:'
        }