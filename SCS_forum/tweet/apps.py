from django.apps import AppConfig

"""
Configures the 'tweet' app with the specified default auto field.
"""
class TweetConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tweet"
