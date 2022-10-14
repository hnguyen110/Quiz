from rest_framework.serializers import ModelSerializer

from quiz_app.models.course_section_item import CourseSectionItem


class CourseSectionItemForAssignedCourseDetailsSectionSerializer(ModelSerializer):
    class Meta:
        model = CourseSectionItem
        fields = ['id', 'order', 'title', 'size', 'content_type']
