from django.db import models

from quiz_app.models.course_section import CourseSection


class CourseSectionItem(models.Model):
    title = models.CharField(max_length=255, null=False)
    order = models.IntegerField(null=False)
    size = models.IntegerField(null=False, default=0)
    content_type = models.CharField(max_length=255, null=True)
    data = models.FileField(upload_to='data', null=True)
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE, related_name='items')

    def delete(self, using=None, keep_parents=False):
        self.data.storage.delete(self.data.name)
        super(CourseSectionItem, self).delete()
