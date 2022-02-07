from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
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
    futon = models.IntegerField('布団の数', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    Queen_bed = models.IntegerField('クイーンベッド', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    semi_Double_bed = models.IntegerField('セミダブルベッド', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    Double_bed = models.IntegerField('ダブルベッド', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    Single_Bed = models.IntegerField('シングルベッド', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    smoking = models.BooleanField('喫煙', default=False)
    open_bath = models.BooleanField('露天風呂', default=False)
    corner_room = models.BooleanField('角部屋', default=False)
    ja_style = models.BooleanField('和室', default=False)
    we_style = models.BooleanField('洋室', default=False)
    dog = models.BooleanField('介助犬', default=False)
    description = models.TextField('説明', default="", blank=True)
    image = models.ImageField(upload_to='images', verbose_name='部屋画像メイン', null=True, blank=True)

    def __str__(self):
        return str(self.house_name) + ':　' + self.room_number

    class Meta:
        verbose_name_plural = 'Room'


class Ticket(models.Model):
    Ticket_number = models.CharField('チケット番号', primary_key=True, max_length=20)
    proprietary = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="所有者", on_delete=models.CASCADE,  null=True, blank=True)
    issue_date = models.DateField('発行日')
    expiry = models.DateField('有効期限')
    ticket_type = models.IntegerField('チケットタイプ', default=0, null=False, blank=False)
    ticket_status = models.BooleanField('利用権限', default=False)


    def __str__(self):
        return str(self.Ticket_number)

    class Meta:
        verbose_name_plural = 'Ticket'



class Reserve(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    reserve_date = models.DateField()
    Ticket_number = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.room_number) + ':　' + str(self.reserve_date)

    class Meta:
        verbose_name_plural = 'Reserve'




class Calendar(models.Model):
    cale_number = models.IntegerField('カレンダー番号', validators=[MinValueValidator(1)], null=True, blank=True)
    date = models.DateField('日付')

    def __str__(self):
        return str(self.cale_number) + ": " + str(self.date)

    class Meta:
        verbose_name_plural = 'Calendar'


class Movie(models.Model):
    # 動画
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
      db_table = 'movie'


class DailyViews(models.Model):
# """日間再生数"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    views = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
      db_table = 'daily_views'