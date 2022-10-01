from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.user_answer import UserAnswer
from quiz_app.serializers.user_answer.base_user_answer_serializer import BaseUserAnswerSerializer
from quiz_app.serializers.user_answer.create_user_answers_serializer import CreateUserAnswersSerializer
from quiz_app.serializers.user_answer.update_user_answers_serializer import UpdateUserAnswersSerializer
from utilities.permissions.is_quiz_participant import IsQuizParticipant


class BaseUserAnswerViewSet(ModelViewSet):
    serializer_class = BaseUserAnswerSerializer
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

    @action(detail=False, methods=['put'], url_path='update_answers')
    def update_answers(self, request, **kwargs):
        serializer = UpdateUserAnswersSerializer(
            data=request.data,
            context={
                'participant_id': kwargs['participant_pk']
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def post_answers(self, request, **kwargs):
        serializer = CreateUserAnswersSerializer(
            data=request.data,
            context={
                'quiz_id': kwargs['quiz_pk'],
                'participant_id': kwargs['participant_pk']
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
