from django.contrib.admin.widgets import AdminDateWidget
from django import forms


room_type = (
    ("1", "ロイヤルルーム"),
    ("2", "デラックスルーム"),
)

class AddUserForm(forms.Form):
    birthday = forms.DateField(widget=forms.SelectDateWidget())
    room = forms.ChoiceField(choices=room_type)
    person = forms.IntegerField(label='大人')
    kids = forms.IntegerField(label='子供')


class ReserveConfirmationForm(forms.Form):
    room_name = forms.CharField(label = '客室')
    room_number = forms.IntegerField(label='室番')
    person = forms.IntegerField(label='大人')
    kids = forms.IntegerField(label='子供')
    Double_bed = forms.IntegerField(label='ダブルベッド')
    Queen_bed = forms.IntegerField(label='クイーン')
    Single_Bed = forms.IntegerField(label='シングルベッド')