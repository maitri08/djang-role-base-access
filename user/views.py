from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from user.models import  (UserRole,Roles,User,Resources)
from user.decorator import CheckPermission
# Create your views here.


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'


class UserLogin():
    def login_user(self,name,password):
        user = authenticate(user=name,password=password)
        if user:
            return ("Logged in as {}".format(name))
        

class RolePermission():
    def create_user(self,**kwargs):
        u,created = User.objects.get_or_create(kwargs['userName'], kwargs['userMail'])
        if created:
            user.set_password(kwargs['passWord'])
            user.save()
            return "New user created"
        else:
            return "User was Retrieved"
            
    def edit_user_role(user, role,  **kwargs):
        get_roles = Roles.objects.filter(pk=kwargs['id'])
        get_roles.access_type = kwargs['access_type']
        get_roles.resource_permission = kwargs['resource_permission']
        get_roles.save()

    def view_roles(user, role,  **kwargs):
        get_roles = Roles.objects.filter(pk=kwargs['id'])
        return get_roles

    def view_resources(user, role,  **kwargs):
        get_roles = Resources.objects.filter(pk=kwargs['id'])
        return get_roles



_choice = {
        1: create_user,
        2: edit_user_role,
        3: view_roles,
        4:view_resources
    }

@CheckPermission
def role_based_acces():
    role_factory = RolePermission()
    role_func = input("Enter the command: ")
    command_type = _choice[role_func]
    return role_factory.command_type()


