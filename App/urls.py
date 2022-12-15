from django.urls import path
from .views import index, singup, tasks

urlpatterns = [
    path('', index, name="index"),   
    path('singup/', singup, name='singup'), # Vista resgistro
    path('tasks/', tasks, name='tasks'), # Vista tareas
]