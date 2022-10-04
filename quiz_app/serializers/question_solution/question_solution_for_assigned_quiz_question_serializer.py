from rest_framework.serializers import ModelSerializer

from quiz_app.models.question_solution import QuestionSolution


class QuestionSolutionForAssignedQuizQuestionSerializer(ModelSerializer):
    class Meta:
        model = QuestionSolution
        fields = ['id', 'description']
