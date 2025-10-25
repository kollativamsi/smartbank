from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, KYC

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']


class KYCForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = ['aadhaar_number', 'pan_number', 'address_proof', 'id_proof', 'selfie']
