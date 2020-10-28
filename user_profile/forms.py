from django.forms import ModelForm, PasswordInput, EmailInput
from django.contrib.auth.models import User
import django.forms as forms


class RegisterForm(ModelForm):
    username = forms.CharField(max_length=100, label="Имя пользователя")
    password = forms.CharField(widget=PasswordInput, label="Пароль")
    email = forms.CharField(widget=EmailInput, label="Email")
    bio = forms.CharField(widget=forms.Textarea, label="О себе", required=False)

    class Meta:
        model = User
        fields = ["username", "password", "email", "bio"]
