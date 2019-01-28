"""
Một test item chứa thông tin về các cases test của người dùng, khi người dùng request một trạng thái test
    + Config các plugin
    + Config các setting cho Plugin
"""
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import pgettext_lazy
from django.utils.translation import ungettext_lazy as _
from robos.models import Setting, Robo
from accounts.models import Account

from common.utils import BACKTESTTYPES

class Trader(models.Model):
    """
    Attributes:
        name: Tên trader
        strategy: Chiến lược sử dụng
        time_start: Thời gian bắt đầu
        time_end: Thời gian kết thúc
        result_file: Kết quả result
        data_file: Kết quả real time trả về
    """
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    name= models.CharField("Tên Trader", max_length = 100)
    time_start = models.DateTimeField('Time Start', null = True)
    time_end = models.DateTimeField('Time End', null = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on= models.DateTimeField( auto_now_add=True)
    
    completed_on= models.DateTimeField( null= True)

    overview = models.CharField("Giới thiệu", max_length = 255, null=True, blank=True)
    note = models.CharField("Ghi chú", max_length = 100, null=True, blank=True)    
    
    def __str__(self):
        return self.name


class TraderSetting(models.Model):
    trader = models.ForeignKey(Trader, on_delete= models.CASCADE, related_name="trader_settings")
    setting = models.ForeignKey(Setting, on_delete = models.CASCADE)
    settingvalue = models.CharField("Setting Value", max_length= 100)