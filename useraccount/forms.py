from django import forms

from django.contrib.auth.models import User #registering new users

from .models import Profile

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)



class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password(self):
        clean_data = self.cleaned_data
        if clean_data['password1'] != clean_data['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return clean_data['password2']



class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget',)