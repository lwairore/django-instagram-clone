from .models import Image

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['uploaded_by','comments', 'likes', 'liked']
        # fields = '__all__'
        
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')