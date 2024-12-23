from django import forms
from .models import Usersinfo

class userform(forms.ModelForm):
    class Meta:
         model=Usersinfo
         fields=["Fullname","Email","Dob","Password","Status"]