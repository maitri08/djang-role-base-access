# Role Based Access Control

Implement a role based auth system. System should be able to assign a role to a user and remove a role from a user.


## Settings

Install using pip:

```bash
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```
#
Added Few Entries in the Database for AccessType,Roles and Resources by using Django Admin or shell command

## Basic Usage
The code requires the User to be logged in order to maintain its authorization id.


```
from user.views import *
role_based_acces()
```

#
_choice = {
        1: create_user,
        2: edit_user_role,
        3: view_roles,
        4:view_resources
    }
#
CheckPermission decorator provides similar behavior to Django's login_required and permission_required decorators. It checks if the user accessing the view does not have the required roles, it will show PERMISSION denied error.
