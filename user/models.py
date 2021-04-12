from django.contrib.auth.models import User
from django.db import models

class AccessType(models.Model):
    READ = 1
    WRITE = 2
    DELETE = 3
    ACCESS_TYPE = (
        (READ, 'Read'),
        (WRITE, 'Write'),
        (DELETE, 'Delete'),
        )
    id = models.PositiveSmallIntegerField(choices=ACCESS_TYPE, primary_key=True)

    def __str__(self):
        return self.get_id_display()
        

class Resources(models.Model):
    name = models.CharField(max_length=50)
    

class Roles(models.Model):
    role = models.CharField(max_length=50)
    access_type = models.ManyToManyField(AccessType, verbose_name="List of Access")
    resource_permission = models.ManyToManyField(Resources, verbose_name="List of Resources")


class UserRole(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role_type = models.ManyToManyField(Roles)


