from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Account(models.Model):
    """
    Thông tin attribute:
    name: tên account
    deposit: số tiền gửi ban đầu. tiền đầu tư
    balance: số dư hiện tại
    description: mô tả chi tiết vê account
    created: user tạo account
    created_on: thời gian tạo
    is_active: trạng thái account

    """
    name = models.CharField(pgettext_lazy("Name of Account", "Name"), max_length=64)
    deposit = models.PositiveIntegerField('số tiền gửi')
    balance = models.IntegerField('Tiền còn lại', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='account_created_by', on_delete=models.CASCADE)
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_on']