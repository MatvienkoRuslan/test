from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.db import models


class UserNAME(models.Model):
    groups = models.ManyToManyField(Group, related_name='custom_group_name')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_permission_name')


class UserModel(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_perms')
    pass
