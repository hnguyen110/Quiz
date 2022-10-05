from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from quiz_app.models.user_answer import UserAnswer


class UpdateUserAnswerSerializer(ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = UserAnswer
        fields = ['id', 'selected_solution']
