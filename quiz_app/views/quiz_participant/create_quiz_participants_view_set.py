from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.quiz_participant import QuizParticipant
from quiz_app.serializers.quiz_participant.create_quiz_participants_serializer import CreateQuizParticipantsSerializer


class CreateQuizParticipantsViewSet(ModelViewSet):
    http_method_names = ['post']
    serializer_class = CreateQuizParticipantsSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return QuizParticipant \
            .objects \
            .filter(quiz_id=self.kwargs['quiz_pk']) \
            .filter(isComplete=False)

    def get_serializer_context(self):
        return {
            'quiz_id': self.kwargs['quiz_pk']
        }
