from django import forms
from .models import Example
# class UserForm(forms.Form):
#     fullname = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     image = forms.ImageField()

class UserForm(forms.ModelForm):
    fullname = forms.CharField(max_length=50, required=True)
    class Meta:
        model = Example
        fields = ['fullname', 'email', 'image']