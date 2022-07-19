from django import forms
from .models import TitleProfile
import datetime
 
# creating a form
class InputForm(forms.Form):
  first_name = forms.CharField(max_length = 200)
  last_name = forms.CharField(max_length = 200)
  # roll_number = forms.IntegerField(help_text = "Enter 6 digit roll")
  # last_modified = forms.DateTimeField(initial = datetime.datetime.now)
#   password = forms.CharField(widget = forms.PasswordInput())
class TitleProfileForm(forms.ModelForm):
    class Meta:
        model = TitleProfile
        fields = "__all__"

