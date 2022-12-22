from django.contrib import admin
from .models import Tasks

class TasksAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )       # Indico campo 'created' como solo lectura y para poder visualizarlo en el admin
                              
admin.site.register(Tasks, TasksAdmin)    # Envio tabla de tarea al admin paso por parametro la clase TaksAdmin