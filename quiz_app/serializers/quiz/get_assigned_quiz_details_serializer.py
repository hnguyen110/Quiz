from rest_framework.serializers import ModelSerializer

from quiz_app.models.quiz import Quiz
from quiz_app.serializers.question.question_for_assigned_quiz_details_serializer import \
    QuestionForAssignedQuizSerializer


class GetAssignedQuizDetailsSerializer(ModelSerializer):
    questions = QuestionForAssignedQuizSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'price', 'questions']
