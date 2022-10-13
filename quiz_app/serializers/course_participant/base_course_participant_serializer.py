from rest_framework.serializers import ModelSerializer

from quiz_app.models.course_participant import CourseParticipant


class BaseCourseParticipantSerializer(ModelSerializer):
    class Meta:
        model = CourseParticipant
        fields = ['id', 'user', 'course']

    def create(self, validated_data):
        course_id = self.context['course_id']
        return CourseParticipant.objects.create(course_id=course_id, **validated_data)

