from django.contrib.auth.forms import UserCreationForm

from accountapp.models import CustomUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'image']