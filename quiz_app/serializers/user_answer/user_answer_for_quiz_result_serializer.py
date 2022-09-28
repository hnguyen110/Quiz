from rest_framework.serializers import ModelSerializer

from quiz_app.models.user_answer import UserAnswer
from quiz_app.serializers.question.question_for_user_answer_serializer import QuestionForUserAnswerSerializer
from quiz_app.serializers.question_solution.base_question_solution_serializer import BaseQuestionSolutionSerializer


class UserAnswerForQuizResultSerializer(ModelSerializer):
    question = QuestionForUserAnswerSerializer()
    selected_solution = BaseQuestionSolutionSerializer()

    class Meta:
        model = UserAnswer
        fields = ['id', 'result', 'question', 'selected_solution']
