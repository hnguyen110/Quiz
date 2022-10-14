from django.db import models

from quiz_app.models.course_section import CourseSection


class CourseSectionItem(models.Model):
    title = models.CharField(max_length=255, null=False)
    order = models.IntegerField(null=False)
    size = models.IntegerField(null=False)
    content_type = models.CharField(max_length=255, null=False)
    data = models.FileField(upload_to='data')
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE, related_name='items')
