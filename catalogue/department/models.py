from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import CoreModel as CM

UserModel = get_user_model()

class Department(CM):
    """
    This are individual units of a Company
    designated to work together accomplish a common goal
    """

    name = models.CharField("name", max_length=128, unique=True, error_messages={'unique': _("A department with that name already exists ;-)")})
    enabled = models.BooleanField(_('enabled'), default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created', 'name', )


# class Profile(CM):
#     """
#     Company employees
#     """

#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
#     employee_id = models.CharField(max_length=128, verbose_name="Employee ID", default=None, null=True, blank=True)
#     title = models.CharField(max_length=128, verbose_name="Title", default=None, null=True, blank=True)
#     notes = models.TextField(_('Asset Description'), max_length=140, blank=True, null=True)
#     site = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     location = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     departments = models.ManyToManyField(Department, verbose_name="departments", blank=True, related_name="profiles")