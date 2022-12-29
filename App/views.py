from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TasksForm
from .models import Tasks
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):                                                 # Vista index para de pagina principal 'home'
    return render(request, 'App/index.html')

@login_required  
def tasks(request):
    search_input = request.POST.get('buscar')
    tasks = Tasks.objects.filter( user = request.user, 
    datecompleted__isnull = True,  ).order_by('-created') # Se genera vista de tareas  
    tasks_completed = Tasks.objects.filter( user = request.user, 
    datecompleted__isnull = True )
    print(search_input)
    if search_input:
        tasks = Tasks.objects.filter( user = request.user, 
        datecompleted__isnull = True, title__startswith = search_input ).order_by('-created')
    return render(request, 'App/tasks.html', {
        'tasks' : tasks,
        'tasks_completed' : tasks_completed,
        'count' : tasks.filter( datecompleted__isnull = True ).count(),
        'search_input' : search_input
    })    

@login_required
def tasks_completed(request):
    search_input = request.POST.get('buscar')
    tasks = Tasks.objects.filter( user = request.user, 
    datecompleted__isnull = False ).order_by( '-datecompleted' ) # Se genera vista de tareas  
    if search_input:
        tasks = Tasks.objects.filter( user = request.user, datecompleted__isnull = False, 
        title__startswith = search_input ).order_by( '-datecompleted' )
    return render(request, 'App/tasks.html', {
        'tasks' : tasks,
        'count' : tasks.filter( datecompleted__isnull = False ).count()
        })                            # Se genera vista de tareas  

@login_required
def create_tasks(request):
    if request.method == 'GET':
        return render(request, 'App/create_tasks.html', {
            'form' : TasksForm
        })
    else:
        try:
            form = TasksForm(request.POST)
            new_task = form.save(commit = False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'App/create_tasks.html', {
                'form' : TasksForm,
                'error' : 'Please provide valida data'
            })    

@login_required
def tasks_detail(request, task_id):
    if request.method == 'GET':
        tasks = get_object_or_404( Tasks, pk=task_id, user = request.user )
        form = TasksForm( instance = tasks )
        return render(request, 'App/tasks_detail.html', {
            'tasks' : tasks, 
            'form' : form
        }) 
    else:
        try:
            tasks = get_object_or_404( Tasks, pk=task_id, user = request.user )
            form = TasksForm( request.POST, instance = tasks )
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'App/tasks_detail.html', {
                'tasks' : tasks,
                'form' : form,
                'error' : 'Error updating task'
            })

@login_required
def complete_tasks(request, task_id):
    tasks = get_object_or_404( Tasks, pk=task_id, user = request.user )
    if request.method == 'POST':
        tasks.datecompleted = timezone.now()
        tasks.save()
        return redirect('tasks')
@login_required
def delete_tasks(request, task_id):
    tasks = get_object_or_404( Tasks, pk=task_id, user = request.user )
    if request.method == 'POST':
        tasks.delete()
        return redirect('tasks')

def signup(request):                                                # Generamos vista Signup para un formulario de registro de usuarios
    if request.method == 'GET':                                     # Se consulta tipo peticion
        return render(request, 'App/signup.html', {
            'form' : UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:  #Consultamos si las contraseñas coinciden las contraseñas
            try:                                                    # Controlamos los posibles errores   
                user = User.objects.create_user(                   
                    request.POST["username"],
                    password=request.POST["password1"])             # Se guardan datos de formulario registro en variable 'user' 
                user.save()                                         # Se guardan los usuarios en DB
                login(request, user)                                # Usuario logeado   
                return redirect('tasks')
            except IntegrityError:                                  # trabajamos con el error 'IntegrityError' este error 
                return render(request, 'App/signup.html', {         # Si existe se renderiza vista signup con mensaje de error
                    'form' : UserCreationForm,
                    'error' : 'Username alredy exists'              # Mensaje de error 'usuario existente'
                })
        return render(request, 'App/signup.html', {
            'form' : UserCreationForm,
            'error' : 'password no match'                           # Mensaje de error al no coincidir la contraseña    
        }) 

def signin(request):                                                # Se crea una funcion para logearse y eneramos vista Signin para un formulario 
    if request.method == 'GET':                                     # Se consulta tipo de peticion
        return render(request, 'App/signin.html', {    
            'form' : AuthenticationForm
        })
    else:
        user = authenticate(                                        # Se guardan datos obtenidos de formulario en variable 'user' 
            request, username=request.POST['username'],
            password=request.POST['password'])
        print(user)
        if user is None:                                            # Se compara datos de registro en variable 'user' con datos de la DB
            return render(request, 'App/signin.html', {             # Si no existe coincidencia en la DB se renderiza vista signin con mensaje de error
                'form' : AuthenticationForm,            
                'error' : 'User or password is incorrect'           # Mensaje de error 'El usuario o la contraseña es incorrecta'
            })
        else:                                                       # Si existe concidencia 
            login(request, user)                                    # Usuario logeado
            return redirect('tasks')                                # Se redirige a vista 'tasks'   

def signout(request):                                               # Se crea una funcion para deslogearse  
    logout(request)                                                 # Deslogueado de usuario        
    return redirect('index')                                        # Al deslogearse se redirecciona al Index 'Home'         
      

    
