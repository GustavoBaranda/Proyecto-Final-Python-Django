from django.urls import path
from .views import index, signup, tasks, signout, signin

urlpatterns = [
    path('', index, name='index'),   
    path('signup/', signup, name='signup'), # Vista resgistro
    path('tasks/', tasks, name='tasks'), # Vista tareas
    path('logout/', signout, name='logout'),
    path('signin/', signin, name='signin'),
]