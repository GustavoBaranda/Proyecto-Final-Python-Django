from django.urls import path
from .views import index, signup, tasks, signout, signin, create_tasks, tasks_detail, complete_tasks, delete_tasks, tasks_completed

urlpatterns = [
    path('', index, name='index'),   
    path('signup/', signup, name='signup'),                          # Vista resgistro
    path('tasks/', tasks, name='tasks'),                             # Vista tareas
    path('tasks_completed/', tasks_completed, name='tasks_completed'),                             # Vista tareas
    path('tasks/create/', create_tasks, name='create_tasks'),        # Vista tareas
    path('tasks/<int:task_id>/', tasks_detail, name='tasks_detail'),        # Vista tareas
    path('tasks/<int:task_id>/complete', complete_tasks, name='complete_tasks'),        # Vista tareas
    path('tasks/<int:task_id>/delete', delete_tasks, name='delete_tasks'),        # Vista tareas
    # path('schedules', schedules, name='schedules'),        # Vista tareas
    path('logout/', signout, name='logout'),                         # cierre de secion
    path('signin/', signin, name='signin'),                          # vista inicio de secion
]