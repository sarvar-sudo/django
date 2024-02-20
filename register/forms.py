from django import forms 

from django.contrib.auth.models import User




class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi userini kiriting..'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi parolini kiriting..'}))
    
class UserRegistrationForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi userini kiriting..'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi emailini kiriting..'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder':'foydalanuvchi parolini kiriting..'}))
    
    
    class Meta:
        model = User
        fields = ['username','email','password']
 