from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_usuarios.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            'email',
            'nome',
            'is_admin',
            'is_comum',
        ]

class EditCustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'nome',
            'is_admin',
            'is_comum',
        ]