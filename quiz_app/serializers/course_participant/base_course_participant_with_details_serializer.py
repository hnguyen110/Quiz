from rest_framework.serializers import ModelSerializer

from quiz_app.models.course_participant import CourseParticipant
from quiz_app.serializers.course.base_course_serializer import BaseCourseSerializer


class BaseCourseParticipantWithDetailsSerializer(ModelSerializer):
    course = BaseCourseSerializer()

    class Meta:
        model = CourseParticipant
        fields = ['id', 'course']
