"""
Module containing the tweet model.

This module contains the model representing a tweet in the forum.
A tweet is composed of a user, a text and an optional photo.
The model also keeps track of the creation and update timestamps of the tweet.

"""

from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.

"""
Model representing a tweet with user, text, photo, creation and update timestamps.

Attributes:
    user (ForeignKey): The user who created the tweet.
    text (TextField): The content of the tweet.
    photo (ImageField): An optional photo attached to the tweet.
    created_at (DateTimeField): The timestamp when the tweet was created.
    updated_at (DateTimeField): The timestamp when the tweet was last updated.

Methods:
    __str__: Returns a string representation of the tweet showing the username and the first 10 characters of the text.
"""


class tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to="photo/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}"


