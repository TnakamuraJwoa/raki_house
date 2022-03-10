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

cal_num = (
    ("1", "No.1"),
    ("2", "No.2"),
    ("3", "No.3"),
    ("4", "No.4"),
    ("5", "No.5"),
    ("6", "No.6"),
    ("7", "No.7"),
    ("8", "No.8"),
    ("9", "No.9"),
    ("10", "No.10"),
    ("11", "No.11"),
    ("12", "No.12"),
    ("13", "No.13"),
    ("14", "No.14"),
    ("15", "No.15"),
    ("16", "No.16"),
    ("17", "No.17"),
    ("18", "No.18"),
    ("19", "No.19"),
    ("20", "No.20"),
    ("21", "No.21"),
    ("22", "No.22"),
    ("23", "No.23"),
    ("24", "No.24"),
    ("25", "No.25"),
    ("26", "No.26"),
    ("27", "No.27"),
    ("28", "No.28"),
    ("29", "No.29"),
    ("30", "No.30"),
    ("31", "No.31"),
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


class CalendarForm(forms.Form):
    cal_num = forms.ChoiceField(choices=cal_num)