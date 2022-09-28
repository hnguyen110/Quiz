from django.db import transaction
from rest_framework import serializers

from quiz_app.models.quiz_participant import QuizParticipant
from quiz_app.serializers.quiz_participant.create_quiz_participant_serializer import CreateQuizParticipantSerializer


class CreateQuizParticipantsSerializer(serializers.Serializer):
    participants = serializers.ListField(child=CreateQuizParticipantSerializer())

    def save(self, **kwargs):
        with transaction.atomic():
            quiz_id = self.context['quiz_id']
            quiz_participants = [
                QuizParticipant(
                    quiz_id=quiz_id,
                    user=participant['user'],
                ) for participant in self.validated_data['participants']
            ]
            return QuizParticipant.objects.bulk_create(quiz_participants)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
