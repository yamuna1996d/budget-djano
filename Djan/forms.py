from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  .models import Income
from  .models import Expenditure

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False, help_text='Optional.')
    password= forms.CharField(max_length=30, required=False, help_text='Optional.')
    confirmpassword= forms.CharField(max_length=30, required=False, help_text='Optional.')
    
class IncomeForm(forms.ModelForm):
    incomeid=forms.CharField(max_length=30,required=False)
    source=forms.CharField(max_length=30,required=False)
    date=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Income
        fields=("incomeid","source","date")
class DetailedForm(forms.ModelForm):
    incomeid=forms.CharField(max_length=30,required=False)
    source=forms.CharField(max_length=30,required=False)
    date=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Income
        fields=("incomeid","source","date")

class Expenditure(forms.ModelForm):
    exid=forms.CharField(max_length=30,required=False)
    source=forms.CharField(max_length=30,required=False)
    date=forms.DateField(widget=forms.SelectDateWidget)


    class Meta:
        model=User
        fields=("username","password")

       

        model=Expenditure
        fields=("exid","source","date")


    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.username = self.cleaned_data["username"]
    #     if commit:
    #         user.save()
    #     return user