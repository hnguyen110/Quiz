from rest_framework.serializers import ModelSerializer

from quiz_app.models.course_section import CourseSection
from quiz_app.serializers.course_section_item.course_section_item_for_assigned_course_details_section_serializer import \
    CourseSectionItemForAssignedCourseDetailsSectionSerializer


class CourseSectionForAssignedCourseDetailsSerializer(ModelSerializer):
    items = CourseSectionItemForAssignedCourseDetailsSectionSerializer(many=True)

    class Meta:
        model = CourseSection
        fields = ['id', 'title', 'items']
