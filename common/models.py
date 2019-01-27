from django.db import models

# Create your models here.

class Profile(models.Model):
    """ Hồ sơ các nhân của user
    """
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField('Họ và tên', max_length = 255)
