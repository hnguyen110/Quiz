from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.question_solution import QuestionSolution
from quiz_app.serializers.question_solution.base_question_solution_serializer import BaseQuestionSolutionSerializer


class BaseQuestionSolutionViewSet(ModelViewSet):
    serializer_class = BaseQuestionSolutionSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return QuestionSolution.objects.filter(question_id=self.kwargs['question_pk'])

    def get_serializer_context(self):
        return {
            'question_id': self.kwargs['question_pk']
        }
