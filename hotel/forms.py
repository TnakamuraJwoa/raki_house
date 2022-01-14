from django.contrib.admin.widgets import AdminDateWidget
from django import forms

class AddUserForm(forms.Form):
    birthday = forms.DateField(widget=forms.SelectDateWidget())