from rest_framework.serializers import ModelSerializer

from quiz_app.models.question import Question
from quiz_app.serializers.question_solution.base_question_solution_serializer import BaseQuestionSolutionSerializer


class QuestionForUserAnswerSerializer(ModelSerializer):
    solutions = BaseQuestionSolutionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'type', 'description', 'solutions']
