"""Robo là thành phần tính toán trên hệ thống,
Khi khai báo, đăng ký một robo lênh hệ thống, admin liệt kê danh sách các plugin,
    Trong plugin có các thông tin input và output

"""
from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _
from common.utils import SETTINGTYPES, PLUGINTYPES
from django.contrib.auth.models import User

# Create your models here.


class Robo(models.Model):
    name = models.CharField("Tên Robo", max_length = 255)
    
    created_on = models.DateTimeField("Ngày tạo", auto_now_add= True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_robos')

class Plugin(models.Model):
    """
    Attributes:
        name: Tên của datafeed
        settings: Các setting của data feed
        robos: Liên kết nhiều nhiều với robo
    """
    name = models.CharField("Tên datafeed", max_length=100)
    kieu = models.CharField('Kiểu plugin', max_length=50, choices = PLUGINTYPES)
    author = models.CharField("Tên tác giả", max_length = 50, null=True, blank = True)
    about = models.CharField("Thông tin tác giả", max_length = 255, null=True, blank=True)
    description = models.CharField("Định nghĩa", max_length = 255, null=True, blank=True)
    inputs = models.CharField("Đầu vào plugin", max_length = 255)
    outputs = models.CharField("Đầu ra plugin", max_length = 255)
    note = models.CharField("Ghi chú", max_length = 255, null=True, blank=True)
    robos = models.ManyToManyField(Robo, related_name='plugins')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on= models.DateTimeField(_("Created on"), auto_now_add=True)
    
    def __str__(self):
        return self.name

# Create your models here.
class Setting(models.Model):
    """ Các setting cho plugin
    Attributes:
        name: Tên của setting
        kieu: Kiểu của setting
    """
    name = models.CharField('Tên Setting', max_length=100)
    kieu = models.CharField('Kiểu Setting', max_length = 50, choices=SETTINGTYPES)
    source = models.CharField('Nguồn', max_length = 50, choices = PLUGINTYPES, default='OTHER')
    defaultvalue = models.CharField('Giá trị mặc định', max_length = 100, null= True, blank = True)
    overview = models.CharField("Giới thiệu", max_length = 255, null=True, blank=True)
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE, null=True, blank=True)
    note = models.CharField("Ghi chú", max_length = 100, null=True, blank=True)
    triger = models.CharField("Ràng buộc các giá trị bang Regex",  max_length = 255, null=True, blank=True)

    def __str__(self):
        return self.name