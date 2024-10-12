"""
This module contains two form classes: `tweetForm` and `UserRegisterForm`.

The `tweetForm` class is a `ModelForm` that is used to create and update
`tweet` objects. It includes fields for the `text` and `photo` fields of the
`tweet` model.

The `UserRegisterForm` class is a `ModelForm` that is used to create new user
accounts. It includes fields for the `username`, `email`, `password1`, and
`password2` fields of the `User` model.
"""


from django import forms
from .models import tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class tweetForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "What's on your mind?", "rows": 3})
    )
    photo = forms.ImageField(required=False)

    class Meta:
        model = tweet
        fields = ["text", "photo"]


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")