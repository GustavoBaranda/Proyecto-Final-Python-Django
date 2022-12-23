from django.urls import path
from .views import index, signup, tasks, signout, signin, create_tasks, tasks_detail

urlpatterns = [
    path('', index, name='index'),   
    path('signup/', signup, name='signup'),                          # Vista resgistro
    path('tasks/', tasks, name='tasks'),                             # Vista tareas
    path('tasks/create/', create_tasks, name='create_tasks'),        # Vista tareas
    path('tasks/<int:task_id>/', tasks_detail, name='tasks_detail'),        # Vista tareas
    path('logout/', signout, name='logout'),                         # cierre de secion
    path('signin/', signin, name='signin'),                          # vista inicio de secion
]