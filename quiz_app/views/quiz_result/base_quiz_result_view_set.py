from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.quiz_participant import QuizParticipant
from quiz_app.serializers.quiz_result.base_quiz_result_serializer import BaseQuizResultSerializer


class BaseQuizResultViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = BaseQuizResultSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return QuizParticipant \
            .objects \
            .filter(quiz_id=self.kwargs['quiz_pk']) \
            .filter(isComplete=True) \
            .prefetch_related('quiz') \
            .prefetch_related('answers__question__solutions') \
            .prefetch_related('answers__selected_solution')
