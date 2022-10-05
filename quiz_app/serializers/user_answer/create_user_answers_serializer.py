from django.db import transaction
from rest_framework import serializers

from quiz_app.models.quiz_participant import QuizParticipant
from quiz_app.models.user_answer import UserAnswer
from quiz_app.serializers.user_answer.create_user_answer_serializer import CreateUserAnswerSerializer


class CreateUserAnswersSerializer(serializers.Serializer):
    answers = serializers.ListField(child=CreateUserAnswerSerializer())

    def save(self, **kwargs):
        with transaction.atomic():
            participant_id = self.context['participant_id']
            answers = [
                UserAnswer(
                    participant_id=participant_id,
                    question=answer['question'],
                    selected_solution=answer['selected_solution']
                ) for answer in self.validated_data['answers']
            ]
            UserAnswer.objects.bulk_create(answers)
            QuizParticipant.objects.filter(pk=participant_id).update(isComplete=True)
            return answers

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
