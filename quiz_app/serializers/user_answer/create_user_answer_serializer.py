from rest_framework.serializers import ModelSerializer

from quiz_app.models.user_answer import UserAnswer


class CreateUserAnswerSerializer(ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['id', 'question', 'selected_solution']
