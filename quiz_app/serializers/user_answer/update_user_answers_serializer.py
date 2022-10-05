from django.db import transaction
from rest_framework import serializers

from quiz_app.models.quiz_participant import QuizParticipant
from quiz_app.models.user_answer import UserAnswer
from quiz_app.serializers.user_answer.update_user_answer_serializer import UpdateUserAnswerSerializer


class UpdateUserAnswersSerializer(serializers.Serializer):
    answers = serializers.ListField(child=UpdateUserAnswerSerializer())

    def save(self, **kwargs):
        with transaction.atomic():
            participant_id = self.context['participant_id']
            answers = [
                UserAnswer(
                    id=answer['id'],
                    selected_solution=answer['selected_solution'],
                    participant_id=participant_id,
                ) for answer in self.validated_data['answers']
            ]
            UserAnswer.objects.bulk_update(answers, ['selected_solution'])
            QuizParticipant.objects.filter(pk=participant_id).update(isComplete=True)
            return answers

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
