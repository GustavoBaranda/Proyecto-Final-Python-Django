from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from .models import Profile_User
from django.dispatch import receiver

@receiver( post_save, sender = User)
def create_profile_user(sender, instance, created, **kwargs):     
    if created:
        Profile_User.objects.create( user = instance) 