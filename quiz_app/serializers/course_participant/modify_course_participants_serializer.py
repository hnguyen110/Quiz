from django.db import transaction
from rest_framework import serializers

from quiz_app.models.course_participant import CourseParticipant
from quiz_app.serializers.course_participant.modify_course_participant_serializer import \
    ModifyCourseParticipantSerializer


class ModifyCourseParticipantsSerializer(serializers.Serializer):
    participants = serializers.ListField(child=ModifyCourseParticipantSerializer())

    def save(self, **kwargs):
        with transaction.atomic():
            course_id = self.context['course_id']
            CourseParticipant.objects.filter(course_id=course_id).delete()
            course_participants = [
                CourseParticipant(
                    course_id=course_id,
                    user=participant['user']
                ) for participant in self.validated_data['participants']
            ]
            return CourseParticipant.objects.bulk_create(course_participants)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
