from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


room_type = (
    ("1", "ロイヤルスイートルーム"),
    ("2", "プレミアムルーム"),
    ("3", "スタンダードルーム"),
)

num_people = (
    ("1", "1名"),
    ("2", "2名"),
    ("3", "3名"),
    ("4", "4名"),
    ("5", "5名"),
    ("6", "6名"),
    ("7", "7名"),
    ("8", "8名"),
    ("9", "9名"),
    ("10", "10名"),
)

num_kids = (
    ("0", "0名"),
    ("1", "1名"),
    ("2", "2名"),
    ("3", "3名"),
    ("4", "4名"),
    ("5", "5名"),
)

class BoxSearchForm(forms.Form):
    room = forms.ChoiceField(choices=room_type)
    person = forms.ChoiceField(choices=num_people)
    kids = forms.ChoiceField(choices=num_kids)
    # person = forms.IntegerField(label='大人')
    # kids = forms.IntegerField(label='子供')
    smoking = forms.BooleanField(help_text='喫煙')
    open_bath = forms.BooleanField(help_text='露天風呂')
    dog = forms.BooleanField(help_text='介護犬')


class ReserveConfirmationForm(forms.Form):
    room_name = forms.CharField(label = '客室', disabled=True)
    room_number = forms.IntegerField(label='室番', disabled=True)
    persons = forms.IntegerField(label='大人', disabled=True)
    kids = forms.IntegerField(label='子供', disabled=True)
    Double_bed = forms.IntegerField(label='ダブルベッド', disabled=True)
    Queen_bed = forms.IntegerField(label='クイーン', disabled=True)
    Single_Bed = forms.IntegerField(label='シングルベッド', disabled=True)