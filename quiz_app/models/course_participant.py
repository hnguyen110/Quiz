from django.conf import settings
from django.db import models

from quiz_app.models.course import Course


class CourseParticipant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='participants')
