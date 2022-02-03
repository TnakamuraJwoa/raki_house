from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class House(models.Model):
    house_name = models.CharField('店舗',  max_length=100)
    address = models.CharField('住所', max_length=100, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=100, null=True, blank=True)
    description = models.TextField('説明', default="", null=True, blank=True)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)

    def __str__(self):
        return self.house_name

    class Meta:
        verbose_name_plural = 'House'

        constraints = [
                    models.UniqueConstraint(fields=['house_name'], name='unique_constraint')
                ]




class Room(models.Model):
    room_number = models.CharField('部屋番号', primary_key=True, max_length=10, null=False, blank=False)
    house_name = models.ForeignKey(House, on_delete=models.CASCADE)
    room_name = models.CharField('部屋名', max_length=30, null=True, blank=False)
    persons = models.IntegerField('大人 - 人数', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    kids = models.IntegerField('子供 - 人数', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    size = models.IntegerField('部屋のサイズ', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    Queen_bed = models.IntegerField('クイーンベッド', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    semi_Double_bed = models.IntegerField('セミダブルベッド', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    Double_bed = models.IntegerField('ダブルベッド', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    Single_Bed = models.IntegerField('シングルベッド', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    smoking = models.BooleanField('喫煙', default=False)
    open_bath = models.BooleanField('露天風呂', default=False)
    corner_room = models.BooleanField('角部屋', default=False)
    ja_style = models.BooleanField('和室', default=False)
    we_style = models.BooleanField('洋室', default=False)
    description = models.TextField('説明', default="", blank=True)
    image = models.ImageField(upload_to='images', verbose_name='部屋画像メイン', null=False, blank=False)

    def __str__(self):
        return self.room_number

    class Meta:
        verbose_name_plural = 'Room'


class Reserve(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    reserve_date = models.DateField()

    def __str__(self):
        return str(self.room_number) + ':　' + str(self.reserve_date)

    class Meta:
        verbose_name_plural = 'Reserve'
