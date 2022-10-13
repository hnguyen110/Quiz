from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.course_participant import CourseParticipant
from quiz_app.serializers.course_participant.base_course_participant_serializer import BaseCourseParticipantSerializer
from quiz_app.serializers.course_participant.modify_course_participant_serializer import \
    ModifyCourseParticipantSerializer


class BaseCourseParticipantViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return CourseParticipant \
            .objects \
            .filter(course_id=self.kwargs['course_pk'], course__owner_id=self.request.user)

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BaseCourseParticipantSerializer
        else:
            return ModifyCourseParticipantSerializer

    def get_serializer_context(self):
        return {
            'course_id': self.kwargs['course_pk']
        }
