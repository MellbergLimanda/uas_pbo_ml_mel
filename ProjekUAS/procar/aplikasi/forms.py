from django import forms
from .models import Mobil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already in use.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class MobilForm(forms.ModelForm):
    class Meta:
        model = Mobil
        fields = ['merek', 'jenis', 'Penggerakroda', 'tahun', 'odometer', 'bahanbakar', 'transmisi', 'kapasitas_mesin', 'warna', 'harga']
