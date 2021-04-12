from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(AccessType)
admin.site.register(Roles)
admin.site.register(Resources)
admin.site.register(UserRole)

