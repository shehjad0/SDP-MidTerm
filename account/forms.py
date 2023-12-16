from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={"id":"required"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"id":"required"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'required'}))
    
    class Meta():
        model= User
        fields=['username', 'first_name', 'last_name', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']