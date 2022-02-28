from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


room_type = (
    ("1", "ロイヤルルーム"),
    ("2", "デラックスルーム"),
)

class BoxSearchForm(forms.Form):
    room = forms.ChoiceField(choices=room_type)
    person = forms.IntegerField(label='大人')
    kids = forms.IntegerField(label='子供')
    stays = forms.IntegerField(label='宿泊数', validators=[MinValueValidator(1), MaxValueValidator(5)])
    smoking = forms.BooleanField(help_text='喫煙')
    open_bath = forms.BooleanField(help_text='露天風呂')
    dog = forms.BooleanField(help_text='介護犬')


class ReserveConfirmationForm(forms.Form):
    room_name = forms.CharField(label = '客室')
    room_number = forms.IntegerField(label='室番')
    person = forms.IntegerField(label='大人')
    kids = forms.IntegerField(label='子供')
    Double_bed = forms.IntegerField(label='ダブルベッド')
    Queen_bed = forms.IntegerField(label='クイーン')
    Single_Bed = forms.IntegerField(label='シングルベッド')