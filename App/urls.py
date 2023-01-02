from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ( 
                    index, signup, tasks, signout, signin, create_tasks,
                    tasks_detail, complete_tasks, delete_tasks, tasks_completed,
                    profile, edit_profile, change_password, delete_user, alert_message,
                    list_of_contact, list_of_contact_detail, create_list_of_contact, 
                    contact, delete_contact
                    )

urlpatterns = [
    path('', index, name='index'),   
    path('signup/', signup, name='signup'),                        
    path('tasks/', tasks, name='tasks'),                             
    path('tasks_completed/', tasks_completed, name='tasks_completed'),                             
    path('tasks/create/', create_tasks, name='create_tasks'),        
    path('tasks/<int:task_id>/', tasks_detail, name='tasks_detail'),        
    path('tasks/<int:task_id>/complete', complete_tasks, name='complete_tasks'),        
    path('tasks/<int:task_id>/delete', delete_tasks, name='delete_tasks'),        
    path('profile/', profile, name='profile'),        
    path('profile/edit_profile/', edit_profile, name='edit_profile'),        
    path('profile/edit_profile/delete_user/', delete_user, name='delete_user'),        
    path('profile/edit_profile/delete_user/alert_message/', alert_message, name='alert_message'),        
    path('list_of_contact/', list_of_contact, name='list_of_contact'), 
    path('list_of_contact/create/', create_list_of_contact, name='create_list_of_contact'),       
    path('list_of_contact/<int:contact_id>/', contact, name='contact'),        
    path('list_of_contact/<int:contact_id>/detail', list_of_contact_detail, name='list_of_contact_detail'),        
    path('list_of_contact/<int:contact_id>/delete_contact', delete_contact, name='delete_contact'),        
    path('change_password/', change_password, name='change_password'),        
    path('logout/', signout, name='logout'),                         
    path('signin/', signin, name='signin'),   
                           
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)