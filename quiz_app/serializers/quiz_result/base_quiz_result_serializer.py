from django.db.models import Sum
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from quiz_app.models.quiz_participant import QuizParticipant
from quiz_app.serializers.quiz.base_quiz_serializer import BaseQuizSerializer
from quiz_app.serializers.user_answer.user_answer_for_quiz_result_serializer import UserAnswerForQuizResultSerializer


class BaseQuizResultSerializer(ModelSerializer):
    class Meta:
        model = QuizParticipant
        fields = ['id', 'isComplete', 'quiz', 'answers', 'overall_result']

    quiz = BaseQuizSerializer()
    answers = UserAnswerForQuizResultSerializer(many=True)
    overall_result = serializers.SerializerMethodField(method_name="get_overall_result")

    @staticmethod
    def get_overall_result(participant: QuizParticipant):
        return participant.answers.aggregate(Sum('result')).get('result__sum', 0)
