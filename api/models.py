import uuid
from django.db import models

# Create your models here.
class path(models.Model):
    path_id = models.UUIDField(uuid.uuid4, primary_key=True)
    path_author = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)