from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
from .models import UserRegistration

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)

    class Meta():
        model = User
        fields=('username','first_name','last_name','email','password1','password2')

    def save(self, commit=True):
        user = super(UserForm ,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user 

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = UserRegistration
        fields = ('is_merchant','address','zipcode','phone','city','state')

