from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model


class CreateUserForm(UserCreationForm):
    employee_id = forms.CharField(
        max_length=255,
        required=False,
        help_text="Enter an unique enployee id.",
    )

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "password1",
            "password2",
            "employee_id",
        )
