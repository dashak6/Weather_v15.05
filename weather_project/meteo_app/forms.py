from django import forms

class AuthForm(forms.Form):
    username = forms.CharField(required=True, label="Логин")
    password = forms.CharField(
        required=True, 
        max_length=32, 
        widget=forms.PasswordInput,
        label="Пароль"
    )