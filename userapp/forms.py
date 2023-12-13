from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class RegistrationForm(UserCreationForm): 
    class Meta:
        model=User
        fields =['first_name', 'username', 'email', 'password1','password2']


class UpdateRegisterForm(forms.ModelForm):

    username = forms.CharField(required=False,
        widget=forms.TextInput( attrs={
        'class':'form-control',
    })
    )

    first_name = forms.CharField(required=False,
        widget=forms.TextInput( attrs={
        'class':'form-control',
    })
    )

    email = forms.EmailField(required=False,
        widget=forms.EmailInput( attrs={
        'class':'form-control',
    })
    )

    class Meta:
        model= User
        fields =[ 'username', 'first_name', 'email']

class UpdateProfileForm(forms.ModelForm):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
 

    gender = forms.ChoiceField(required=False,
        choices=GENDER,
        widget=forms.Select( attrs={
        
        'class':'form-control',
    })
    )

    address = forms.CharField(required=False,
        widget=forms.TextInput( attrs={
        'class':'form-control',
    })
    )

    phone = forms.IntegerField(required=False,
        widget=forms.NumberInput( attrs={
        'class':'form-control',
    })
    )

    image = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)
