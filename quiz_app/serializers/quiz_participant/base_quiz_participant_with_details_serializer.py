from rest_framework.serializers import ModelSerializer

from quiz_app.models.quiz_participant import QuizParticipant
from quiz_app.serializers.quiz.base_quiz_serializer import BaseQuizSerializer


class BaseQuizParticipantWithDetailsSerializer(ModelSerializer):
    quiz = BaseQuizSerializer()

    class Meta:
        model = QuizParticipant
        fields = ['id', 'quiz', 'isComplete']
