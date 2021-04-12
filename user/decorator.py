from django.contrib.auth.decorators import user_passes_test
from user.models import UserRole


class CheckPermission():
    """
    Decorator for views that checks whether a user has a particular role,
    """
    def __init__(self, function):
        self.function = function
  
    def __call__(self, *params):
        role_table = UserRole.objects.filter(user__id=user_id).prefetch_related('role_type')

        if any([True for i in role_table if *params in i]):
            return self.function(*params)
        else:
            raise TypeError("User Does Not Have Permission !!")