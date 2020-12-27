from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post,Hotel

class CreateUserForm(UserCreationForm):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover']


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['Bio', 'hotel_Main_Img']







