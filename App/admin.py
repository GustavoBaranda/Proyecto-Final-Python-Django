from django.contrib import admin
from .models import Tasks, List_of_contact, Profile_User

class TasksAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )       # Indico campo 'created' como solo lectura y para poder visualizarlo en el admin
                              
admin.site.register( Tasks, TasksAdmin )    # Envio tabla de tarea al admin paso por parametro la clase TaksAdmin
admin.site.register( List_of_contact )    # Envio tabla de tarea al admin paso por parametro la clase TaksAdmin
admin.site.register( Profile_User )    # Envio tabla de tarea al admin paso por parametro la clase TaksAdmin


