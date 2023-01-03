
from django import forms
from .models import Tasks, Profile_User, List_of_contact
from django.contrib.auth.models import User

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'important']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),
            'important' : forms.CheckboxInput(attrs={'class' : 'form-check-input'}),
        }
        labels = {
            'title': 'Titulo:',
            'description' : 'Descripcion:',
            'important' : 'Importate ',
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name' ,'email'] 
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
            
        }
        labels = {
            'username': 'Usuario:',
            'first_name' : 'Nombre:',
            'last_name' : 'Apellido:',
            'email' : 'Correo:'
        }       

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile_User
        fields = ['image']
        widgets = {
            'image' : forms.FileInput(attrs={'class' : 'form-control btn btn-secondary'}),
        }
        labels = {
            'image': 'image:',
        }     

class ContactForm(forms.ModelForm):
    class Meta:
        model = List_of_contact
        fields = ['name','last_name','phone', 'adress', 'email'] 
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'phone' : forms.TextInput(attrs={'class' : 'form-control'}),
            'adress' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
        }
        labels = {
            'name': 'Nombre:',
            'last_name' : 'Apellido:',
            'phone' : 'Telefono:',
            'adress' : 'Domicilio:',
            'email' : 'Correo:',
        }
        