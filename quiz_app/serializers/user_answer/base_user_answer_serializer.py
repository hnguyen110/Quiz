from rest_framework import serializers, status
from rest_framework.exceptions import APIException
from rest_framework.serializers import ModelSerializer

from quiz_app.models.quiz import Quiz
from quiz_app.models.user_answer import UserAnswer


class BaseUserAnswerSerializer(ModelSerializer):
    result = serializers.FloatField(read_only=True)
    participant = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserAnswer
        fields = ['id', 'result', 'question', 'selected_solution', 'participant']

    def create(self, validated_data):
        participant_id = self.context['participant_id']
        options_are_valid = Quiz \
            .objects \
            .filter(pk=self.context['quiz_id']) \
            .filter(questions__solutions__in=[validated_data['selected_solution']]) \
            .filter(questions__in=[validated_data['question']]) \
            .exists()
        if not options_are_valid:
            raise APIException(detail='Selected question or solution is not valid',
                               code=status.HTTP_400_BAD_REQUEST)

        return UserAnswer \
            .objects \
            .create(participant_id=participant_id, **validated_data)
