from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.quiz_participant import QuizParticipant
from quiz_app.serializers.quiz_participant.base_quiz_participant_serializer import BaseQuizParticipantSerializer
from quiz_app.serializers.quiz_result.base_quiz_result_serializer import BaseQuizResultSerializer
from utilities.permissions.is_quiz_participant import IsQuizParticipant


class BaseQuizParticipantViewSet(ModelViewSet):
    serializer_class = BaseQuizParticipantSerializer
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

    @action(detail=True, methods=['get'], url_path='results', permission_classes=[IsQuizParticipant])
    def get_submitted_quizzes(self, request, **kwargs):
        quiz_result = get_object_or_404(
            QuizParticipant
            .objects
            .filter(quiz_id=self.kwargs['quiz_pk'], isComplete=True)
            .prefetch_related('quiz')
            .prefetch_related('answers__question__solutions')
            .prefetch_related('answers__selected_solution'),
            pk=self.kwargs['pk'])
        serializer = BaseQuizResultSerializer(quiz_result)
        return Response(serializer.data, status=status.HTTP_200_OK)
