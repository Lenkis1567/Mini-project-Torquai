from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrerUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','last_name', 'first_name', 'email')
        
# class UserAuthenticationForm (AuthenticationForm):
#     class Meta:
#         mofel
