from django.db import models
# Create your models here.

class House(models.Model):
    name = models.CharField('店舗', max_length=100)
    address = models.CharField('住所', max_length=100, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=100, null=True, blank=True)
    description = models.TextField('説明', default="", blank=True)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'House'
        def __str__(self):
            return self.name



class Room(models.Model):
    room_number = models.CharField('部屋番号', max_length=10, null=True, blank=True)
    room_name = models.CharField('部屋名', max_length=30, null=True, blank=True)
    persons = models.IntegerField('大人 - 人数', default=0, null=True, blank=True)
    kids = models.IntegerField('子供 - 人数', default=0, null=True, blank=True)
    size = models.IntegerField('部屋のサイズ', default=0, null=True, blank=True)
    Queen_bed = models.IntegerField('クイーンベッド', default=0, null=True, blank=True)
    Double_bed = models.IntegerField('ダブルベッド', default=0, null=True, blank=True)
    Single_Bed = models.IntegerField('シングルベッド', default=0, null=True, blank=True)
    smoking = models.BooleanField('喫煙', default=False)
    description = models.TextField('説明', default="", blank=True)
    image = models.ImageField(upload_to='images', verbose_name='部屋画像メイン', null=True, blank=True)
    in_date = models.DateField('チェックイン', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Room'

        def __str__(self):
            return self.name