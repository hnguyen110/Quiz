from rest_framework.serializers import ModelSerializer

from quiz_app.models.quiz_participant import QuizParticipant
from quiz_app.serializers.quiz.base_quiz_serializer import BaseQuizSerializer
from quiz_app.serializers.user_answer.user_answer_for_quiz_result_serializer import UserAnswerForQuizResultSerializer


class BaseQuizResultSerializer(ModelSerializer):
    quiz = BaseQuizSerializer()
    answers = UserAnswerForQuizResultSerializer(many=True)

    class Meta:
        model = QuizParticipant
        fields = ['id', 'isComplete', 'quiz', 'answers']
