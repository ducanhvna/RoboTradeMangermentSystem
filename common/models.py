from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    """ Hồ sơ các nhân của user
    """
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    name = models.CharField('Họ và tên', max_length = 255)
