#from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """拡張ユーザモデル"""
    member_id = models.CharField(verbose_name='会員番号', unique=True, max_length=10)
    gender = models.IntegerField('性別', null=True, blank=True)
    member_type = models.IntegerField('メンバータイプ', null=True, blank=True)



    def __str__(self):
        return self.member_id

    class Meta:
        verbose_name_plural = 'CustomUser'

