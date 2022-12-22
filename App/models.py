from django.db import models 
from django.contrib.auth.models import User 

class Tasks(models.Model):                                       # Se crea una tabla para las tareas
    title = models.CharField( max_length = 100 )                 # Se crea campo de tipo caracter con maximo de 100 caracteres para el titulo de la tarea 
    description = models.TextField( blank = True )               # Se crea campo de texto para descripcion de la tarea
    created = models.DateTimeField( auto_now_add = True )        # Se crea un campo para registrar el momento actual en que se crea la tarea
    datecompleted = models.DateTimeField( null = True, blank = True )          # Se crea un campo para registrar fecha de tarea cumplida 
    important = models.BooleanField( default = True )            # Se crea un campo check para indicar si latarea es importante 
    user = models.ForeignKey( User, on_delete = models.CASCADE ) # Se crea un campo user para vincular con la DB de user 

    def __str__(self):
        return self.title + ' - by ' + self.user.username        # se retorna titulo de la tarea y usuario que la creo
