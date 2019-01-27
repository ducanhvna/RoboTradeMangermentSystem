from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Account(models.Model):
    name = models.CharField(pgettext_lazy("Name of Account", "Name"), max_length=64)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='account_created_by', on_delete=models.CASCADE)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_on']