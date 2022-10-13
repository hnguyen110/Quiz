from django.db import models

from quiz_app.models.course_section import CourseSection


class SectionItem(models.Model):
    title = models.CharField(max_length=255, null=False)
    content_type = models.CharField(max_length=255, null=False)
    size = models.IntegerField(null=False)
    order = models.IntegerField(null=False)
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE, related_name='items')
