from django import forms
from .models import Signup, Login

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    verify_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Signup
        fields = '__all__'

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = '__all__'
