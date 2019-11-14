from django import forms
from django.contrib.auth.forms import UserCreateForm
from django.contrib.auth.models import User

class UserCreateForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False, help_text='Optional.')
    password= forms.CharField(max_length=30, required=False, help_text='Optional.')
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirmpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=("username","password")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user