from django.conf import settings
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
