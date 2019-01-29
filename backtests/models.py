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

from common.utils import BACKTESTTYPES

class BackTest(models.Model):
    """
    Attributes:
        name: Testitem
        datafeed: datafeed plugin sử dụng
        strategy: Chiến lược sử dụng
        time_start: Thời gian bắt đầu
        time_end: Thời gian kết thúc
        result_file: Kết quả result
        data_file: Kết quả real time trả về
    """
    name= models.CharField("Tên item", max_length = 100)
    time_start = models.DateTimeField('Time Start', null = True)
    time_end = models.DateTimeField('Time End', null = True)
    status= models.CharField('Trạng thái', max_length = 50, choices = BACKTESTTYPES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on= models.DateTimeField( auto_now_add=True)

    completed_on= models.DateTimeField( null= True)
    settings = models.ManyToManyField(Setting, through='TestSetting', related_name='backtests')
    overview = models.CharField("Giới thiệu", max_length = 255, null=True, blank=True)
    note = models.CharField("Ghi chú", max_length = 100, null=True, blank=True)    
    
    def __str__(self):
        return self.name


class TestSetting(models.Model):
    backtest = models.ForeignKey(BackTest, on_delete= models.CASCADE, related_name="backtest_settings")
    setting = models.ForeignKey(Setting, on_delete = models.CASCADE)
    settingvalue = models.CharField("Setting Value", max_length= 100)

class TestResult(models.Model):
    backtest = models.ForeignKey(BackTest, on_delete=models.CASCADE, related_name='results')

    time_start = models.DateTimeField('Time Start', null = True)
    time_end = models.DateTimeField('Time End', null = True)

    result_file = models.FileField(upload_to='results/%Y/%m/%d/', blank=True)
    data_file = models.FileField(upload_to='data/%Y/%m/%d/', blank=True)
    created_on= models.DateTimeField(auto_now_add=True)
    note = models.CharField("Ghi chú", max_length = 100, null=True, blank=True)    