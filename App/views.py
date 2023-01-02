from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TasksForm, UserUpdateForm, ProfileUpdateForm, ContactForm
from .models import Tasks, List_of_contact 
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(request):
                                                     # Vista index para de pagina principal 'home'
    return render(request, 'App/index.html')

@login_required  
def tasks(request):
    search_input = request.POST.get('buscar')
    tasks = Tasks.objects.filter( user = request.user, 
    datecompleted__isnull = True,  ).order_by('-created') 
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
                'error' : 'Error de actualizacion de tareas'
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
                user = User.objects.create_user( username = request.POST["username"],
                    first_name = request.POST["first_name"],
                    last_name = request.POST["last_name"],
                    email = request.POST["email"],
                    password = request.POST["password1"])             # Se guardan datos de formulario registro en variable 'user' 
                user.save()                                         # Se guardan los usuarios en DB
                login(request, user)                                # Usuario logeado   
                return redirect('tasks')
            except IntegrityError:                                  # trabajamos con el error 'IntegrityError' este error 
                return render(request, 'App/signup.html', {         # Si existe se renderiza vista signup con mensaje de error
                    'form' : UserCreationForm,
                    'error' : 'El ususario ya existe'              # Mensaje de error 'usuario existente'
                })
        return render(request, 'App/signup.html', {
            'form' : UserCreationForm,
            'error' : 'Las contraseñas no coinciden'                           # Mensaje de error al no coincidir la contraseña    
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
                'error' : 'El Usuario o contarseña no coinciden'           # Mensaje de error 'El usuario o la contraseña es incorrecta'
            })
        else:                                                       # Si existe concidencia 
            login(request, user)                                    # Usuario logeado
            return redirect('tasks')                                # Se redirige a vista 'tasks'   

def signout(request):                                               # Se crea una funcion para deslogearse  
    logout(request)                                                 # Deslogueado de usuario        
    return redirect('index') 

@login_required    
def profile(request):
    profile = request.user
    return render(request, 'App/profile.html', {
        'profile' : profile
    })  

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm( request.POST, instance = request.user )
        p_form = ProfileUpdateForm( request.POST, request.FILES, instance = request.user.profile_user)
        
        if u_form.is_valid() and p_form.is_valid():
            print('es valido')
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm( instance = request.user )
        p_form = ProfileUpdateForm() 
        return render(request, 'App/edit_profile.html', {
            'u_form' : u_form,
            'p_form' : p_form
        })       
        
    return render(request, 'App/edit_profile.html', {
        'u_form' : u_form,
        'p_form' : p_form
    })

@login_required 
def change_password(request):
    if request.method == 'GET':                                   
        return render(request, 'App/change_password.html')
    else:
        if request.POST["password1"] == request.POST["password2"]:  
            user = User.objects.filter( id = request.user.id )
            if user.exists():
                user = user.first()
                user.set_password(request.POST["password1"])
                user.save()
                logout(request)
                return redirect('signin')
            else:
                return  redirect('profile')  
        else:
            return render(request, 'App/change_password.html', {
                'error' : 'Las contraseñas no coinciden'
            })   

@login_required
def delete_user(request):
    user = User.objects.filter( id = request.user.id )
    if user.exists():
        user.delete()
        return redirect('signin')  

@login_required
def alert_message(request):
    return render(request, 'App/delete_user.html')

@login_required  
def list_of_contact(request):
    search_input = request.POST.get('buscar')
    contact = List_of_contact.objects.filter( user = request.user ).order_by('last_name') 
    if search_input:
        contact = List_of_contact.objects.filter( 
            Q(name__contains = search_input) | 
            Q(last_name__contains =  search_input) ).order_by('-name')
    return render(request, 'App/list_of_contact.html', {
        'contact' : contact,
        'search_input' : search_input
    })

def contact(request, contact_id):
    if request.method == 'GET':
        contact = get_object_or_404( List_of_contact, pk=contact_id, user = request.user )
        return render(request, 'App/contact.html', {
            'contact' : contact, 
           
        }) 
    else:
        try:
            contact = get_object_or_404( List_of_contact, pk = contact_id, user = request.user )
            form = ContactForm( request.POST, instance = contact )
            form.save()
            return redirect('list_of_contact')
        except ValueError:
            return render(request, 'App/contact.html', {
                'contact' : contact,
                'form' : form,
                'error' : 'Error de actualizacion de contacto'
            })    

@login_required
def create_list_of_contact(request):
    if request.method == 'GET':
        return render(request, 'App/create_list_of_contact.html', {
            'form' : ContactForm
        })
    else:
        try:
            form = ContactForm(request.POST)
            new_list_of_contact = form.save(commit = False)
            new_list_of_contact.user = request.user
            new_list_of_contact.save()
            return redirect('list_of_contact')
        except ValueError:
            return render(request, 'App/create_list_of_contact.html', {
                'form' : ContactForm,
                'error' : 'Please provide valida data'
            })    
   
@login_required
def list_of_contact_detail(request, contact_id):
    if request.method == 'GET':
        contact = get_object_or_404( List_of_contact, pk=contact_id, user = request.user )
        form = ContactForm( instance = contact )
        return render(request, 'App/list_of_contact_detail.html', {
            'contact' : contact, 
            'form' : form
        }) 
    else:
        try:
            contact = get_object_or_404( List_of_contact, pk = contact_id, user = request.user )
            form = ContactForm( request.POST, request.FILES, instance = contact )
            if form.is_valid():
                form.save()
                return redirect('contact', contact.id)
        except ValueError:
            return render(request, 'App/list_of_contact_detail.html', {
                'contact' : contact,
                'form' : form,
                'error' : 'Error de actualizacion de contacto'
            })    

@login_required
def delete_contact(request, contact_id):
    contact = get_object_or_404( List_of_contact, pk = contact_id, user = request.user )
    if request.method == 'POST':
        contact.delete()
        return redirect('list_of_contact')    


