from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

class UploadProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','description','project_url','technologies','project_image')

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields=['design','content','usability'] 

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')  
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name',  'bio', 'location', 'account_url' ,'prof_pic')