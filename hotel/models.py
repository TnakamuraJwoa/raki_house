from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from accounts.models import CustomUser
# Create your models here.

class House(models.Model):
    house_name = models.CharField('店舗',  unique=True, max_length=100)
    address = models.CharField('住所', max_length=100, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=100, null=True, blank=True)
    description = models.TextField('説明', default="", null=True, blank=True)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)

    def __str__(self):
        return self.house_name

    class Meta:
        verbose_name_plural = 'House'

        # constraints = [
        #             models.UniqueConstraint(fields=['house_name'], name='unique_constraint')
        #         ]




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
    room_active = models.BooleanField('アクティブ', default=False)

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
    Representative_name = models.CharField('代表者名', max_length=20, null=True, blank=True)
    reserve_date = models.DateField()
    Ticket_number = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    member_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.room_number) + ':　' + str(self.reserve_date)

    class Meta:
        verbose_name_plural = 'Reserve'




class Calendar(models.Model):
    member_id = models.ForeignKey(CustomUser, verbose_name="所有者", on_delete=models.SET_DEFAULT, default='不明')
    no = models.IntegerField('チケット番号', validators=[MinValueValidator(0)], default=0, null=False, blank=False)
    date = models.DateField('日付')
    used = models.BooleanField('使用済', default=False)
    cal_active = models.BooleanField('アクティブ', default=False)

    def __str__(self):
        return str(self.no) + ': ' + str(self.date)

    class Meta:
        verbose_name_plural = 'Calendar'



class RFourCalendar(models.Model):
    no = models.IntegerField('no', null=False, blank=False)
    no_sub = models.IntegerField('no_sub', null=False, blank=False)
    Jan = models.DateField('1月', null=True, blank=True)
    Feb = models.DateField('2月', null=True, blank=True)
    Mar = models.DateField('3月', null=True, blank=True)
    Apr = models.DateField('4月', null=True, blank=True)
    May = models.DateField('5月', null=True, blank=True)
    Jun = models.DateField('6月', null=True, blank=True)
    Jul = models.DateField('7月', null=True, blank=True)
    Aug = models.DateField('8月', null=True, blank=True)
    Sep = models.DateField('9月', null=True, blank=True)
    Oct = models.DateField('10月', null=True, blank=True)
    Nov = models.DateField('11月', null=True, blank=True)
    Dec = models.DateField('12月', null=True, blank=True)

    def __str__(self):
        return str(self.no) + "-" + str(self.no_sub)

    class Meta:
        verbose_name_plural = 'RFourCalendar'
