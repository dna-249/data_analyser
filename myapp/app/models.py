from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=200)
    dynamic_data = models.JSONField(default=dict)
    