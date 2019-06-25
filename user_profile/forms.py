from homepage.models import Profile, Image
from django import forms

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id', 'bio', 'user_id', 'first_name', 'last_name', 'email', 'phone', 'mobile']
        # fields = '__all__'


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['uploaded_by','comments', 'likes', 'liked']
        # fields = '__all__'
        