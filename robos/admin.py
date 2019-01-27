from django.contrib import admin
from robos.models import Robo, Plugin, Setting
# Register your models here.

admin.site.register(Robo)
admin.site.register(Plugin)
admin.site.register(Setting)