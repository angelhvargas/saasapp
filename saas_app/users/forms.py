from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from saas_app.users.models import User


class MyUserCreationForm(UserCreationForm):

    field_order = ["first_name", "email"]

    class Meta(UserCreationForm):
        model = User
        fields = ("first_name", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email  # Use email as username
        if commit:
            user.save()
        return user