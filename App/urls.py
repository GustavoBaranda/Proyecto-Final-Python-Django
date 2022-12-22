from django.urls import path
from .views import index, signup, tasks, signout, signin, create_tasks

urlpatterns = [
    path('', index, name='index'),   
    path('signup/', signup, name='signup'),                          # Vista resgistro
    path('tasks/', tasks, name='tasks'),                             # Vista tareas
    path('tasks/create/', create_tasks, name='create_tasks'),        # Vista tareas
    path('logout/', signout, name='logout'),                         # cierre de secion
    path('signin/', signin, name='signin'),                          # vista inicio de secion
]