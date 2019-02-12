from django.contrib import admin
from backtests.models import BackTest, TestSetting
# Register your models here.

admin.site.register(BackTest)
admin.site.register(TestSetting)
