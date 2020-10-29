from django.forms import ModelForm, PasswordInput, EmailInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import django.forms as forms


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, label="Имя пользователя")
    email = forms.CharField(widget=EmailInput, label="Email")
    bio = forms.CharField(widget=forms.Textarea, label="О себе", required=False)
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "bio"]
