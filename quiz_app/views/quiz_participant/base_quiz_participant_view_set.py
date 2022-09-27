from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.quiz_participant import QuizParticipant
from quiz_app.serializers.quiz_participant.base_quiz_participant_serializer import BaseQuizParticipantSerializer


class BaseQuizParticipantViewSet(ModelViewSet):
    serializer_class = BaseQuizParticipantSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return QuizParticipant.objects.filter(quiz_id=self.kwargs['quiz_pk'])

    def get_serializer_context(self):
        return {
            'quiz_id': self.kwargs['quiz_pk']
        }
