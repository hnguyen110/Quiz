from rest_framework.serializers import ModelSerializer

from quiz_app.models.question import Question
from quiz_app.serializers.question_solution.question_solution_for_assigned_quiz_question_serializer import \
    QuestionSolutionForAssignedQuizQuestionSerializer


class QuestionForAssignedQuizSerializer(ModelSerializer):
    solutions = QuestionSolutionForAssignedQuizQuestionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'type', 'description', 'solutions']
