from rest_framework.serializers import ModelSerializer

from quiz_app.models.course import Course
from quiz_app.serializers.course_section.course_section_for_assigned_course_details_serializer import \
    CourseSectionForAssignedCourseDetailsSerializer


class AssignedCourseDetailsSerializer(ModelSerializer):
    sections = CourseSectionForAssignedCourseDetailsSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'sections']
