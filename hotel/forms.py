from django.contrib.admin.widgets import AdminDateWidget
from django import forms


room_type = (
    ("1", "ファミリータイプ"),
    ("2", "クイーンルーム"),
    ("3", "シングルルーム"),
)

class AddUserForm(forms.Form):
    birthday = forms.DateField(widget=forms.SelectDateWidget())
    room = Checkbox = forms.ChoiceField(choices=room_type)
    person = forms.IntegerField(label='大人')
    kids = forms.IntegerField(label='子供')