from django import forms
from django.db.models.base import Model
from .models import Comment, Post, Profile
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
# Create your models here.


class ProfileUpdate(ModelForm):
    class Meta:
        model = Profile
        fields = ['last_name', 'first_name', 'email', 'profile_image']

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',}))

class CreateComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'picture']

        