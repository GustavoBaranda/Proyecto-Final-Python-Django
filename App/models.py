from django.db import models 
from django.contrib.auth.models import User 

class Tasks(models.Model):                                      # Se crea una tabla para las tareas
    title = models.CharField( max_length = 100 )                # Se Crea campo 
    description = models.TextField( blank = True )
    created = models.DateTimeField( auto_now_add = True )
    datecompleted = models.DateTimeField( null = True )
    important = models.BooleanField( default = True )
    user = models.ForeignKey( User, on_delete = models.CASCADE )

    def __str__(self):
        return self.title + ' - by ' + self.user.username
