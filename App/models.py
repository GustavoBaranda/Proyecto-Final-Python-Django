from django.db import models 
from django.contrib.auth.models import User 

class Profile_User(models.Model):
    user = models.OneToOneField( User, on_delete = models.CASCADE)
    image = models.ImageField( default = 'user.png')
    
    def __str__(self):
        return f'Perfil de {self.user.username}'        

class Tasks(models.Model):                                      
    title = models.CharField( max_length = 100 )                 
    description = models.TextField( blank = True )              
    created = models.DateTimeField( auto_now_add = True )       
    datecompleted = models.DateTimeField( null = True, blank = True ) 
    important = models.BooleanField( default = True )             
    user = models.ForeignKey( User, on_delete = models.CASCADE )  

    def __str__(self):
        return self.title + ' - by ' + self.user.username        

class List_of_contact(models.Model):
    name = models.CharField( max_length = 100 )
    last_name = models.CharField( max_length = 100)
    phone = models.IntegerField()
    adress = models.CharField( max_length = 100, blank = True )
    email = models.CharField( max_length= 100, blank = True )
    user = models.ForeignKey( User, on_delete = models.CASCADE )
    image_contact = models.ImageField( default = 'user.png')
    
    def __str__(self):
        return self.last_name + ', '+ self.name +' - by ' + self.user.username
