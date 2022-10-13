from django.db import models

from quiz_app.models.course import Course


class CourseSection(models.Model):
    title = models.CharField(max_length=255, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
