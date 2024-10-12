"""
Admin configuration for the tweet app.

Registers the tweet model with the admin site.
"""


from django.contrib import admin
from .models import tweet

admin.site.register(tweet)

