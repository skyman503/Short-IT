from django.db import models

# Url Model
class UrlModel(models.Model):
    old_url = models.CharField(max_length=500)
    new_url = models.CharField(max_length=16, null=True, default='xyz')

