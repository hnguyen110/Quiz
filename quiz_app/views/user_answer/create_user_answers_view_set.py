from rest_framework.viewsets import ModelViewSet

from quiz_app.models.user_answer import UserAnswer
from quiz_app.serializers.user_answer.create_user_answers_serializer import CreateUserAnswersSerializer
from utilities.permissions.is_quiz_participant import IsQuizParticipant


class CreateUserAnswersViewSet(ModelViewSet):
    http_method_names = ['post']
    serializer_class = CreateUserAnswersSerializer
    permission_classes = [IsQuizParticipant]

    def get_queryset(self):
        return UserAnswer \
            .objects \
            .filter(participant=self.kwargs['participant_pk']) \
            .filter(participant__isComplete=False) \
            .select_related('participant__user')

    def get_serializer_context(self):
        return {
            'quiz_id': self.kwargs['quiz_pk'],
            'participant_id': self.kwargs['participant_pk']
        }
