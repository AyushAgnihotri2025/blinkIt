import uuid
from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=lambda i, f: '/'.join(['images', f'{uuid.uuid4().hex}.{f.partition(".")[2]}']))
    uploaded_at = models.DateTimeField(auto_now_add=True)
