from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def index(request):                                                 # Vista index para de pagina principal 'home'
    return render(request, 'App/index.html')

def signup(request):                                                # Generamos vista Signup para un formulario de registro de usuarios
    if request.method == 'GET':                                     # Se consulta tipo de metodo del formulario de registro
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
            except IntegrityError:                                  # Compruebamos si existe un usuario con el mismo nombre  
                return render(request, 'App/signup.html', {         # Si existe se renderiza vista signup con mensaje de error
                    'form' : UserCreationForm,
                    'error' : 'Username alredy exists'              # Mensaje de error 'usuario existente'
                })
        return render(request, 'App/signup.html', {
            'form' : UserCreationForm,
            'error' : 'password no match'                           # Mensaje de error al no coincidir la contraseña    
        }) 

  
def tasks(request):                                                 # Se genera vista de tareas  
    return render(request, 'App/tasks.html')


def signout(request):                                               # Se crea una funcion para deslogearse  
    logout(request)                                                 # Deslogueado de usuario        
    return redirect('index')                                        # Al deslogearse se redirecciona al Index 'Home'    

def signin(request):                                                # Se crea una funcion para logearse y eneramos vista Signin para un formulario 
    if request.method == 'GET':                                     # Se consulta tipo de metodo del formulario de logeo
        return render(request, 'App/signin.html', {    
            'form' : AuthenticationForm
        })
    else:
        user = authenticate(                                        # Se guardan datos obtenidos de formulario en variable 'user' 
            request, username=request.POST['username'], 
            pasword=request.POST['password'])

        if user is None:                                            # Se compara datos de registro en variable 'user' con datos de la DB
            return render(request, 'App/signin.html', {             # Si no existe coincidencia en la DB se renderiza vista signin con mensaje de error
                'form' : AuthenticationForm,            
                'error' : 'User or password is incorrect'           # Mensaje de error 'El usuario o la contraseña es incorrecta'
            })
        else:                                                       # Si existe concidencia 
            login(request, user)                                    # Usuario logeado
            return redirect('tasks')                                # Se redirige a vista 'tasks'   
     
      

    
