from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.question import Question
from quiz_app.serializers.question.base_question_serializer import BaseQuestionSerializer


class BaseQuestionViewSet(ModelViewSet):
    serializer_class = BaseQuestionSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Question.objects.filter(quiz_id=self.kwargs['quiz_pk'])

    def get_serializer_context(self):
        return {
            'quiz_id': self.kwargs['quiz_pk']
        }
