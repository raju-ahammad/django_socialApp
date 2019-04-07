from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        exclude = ('username' ,)
        fields = ['username', 'first_name', 'last_name',]    
