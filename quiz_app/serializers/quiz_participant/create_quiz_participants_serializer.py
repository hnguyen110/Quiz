from django.db import transaction
from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from quiz_app.models.quiz_participant import QuizParticipant


class CreateQuizParticipantsSerializer(serializers.Serializer):
    participants = serializers.ListField(child=serializers.IntegerField())

    def save(self, **kwargs):
        with transaction.atomic():
            quiz_id = self.context['quiz_id']
            is_participant_assigned = QuizParticipant \
                .objects \
                .filter(user_id__in=self.validated_data['participants']) \
                .filter(quiz_id=quiz_id) \
                .exists()
            if is_participant_assigned:
                raise APIException(detail="One or more participants have already been assigned to the quiz",
                                   code=status.HTTP_400_BAD_REQUEST)

            quiz_participants = [
                QuizParticipant(
                    quiz_id=quiz_id,
                    user_id=participant_id,
                    isComplete=False
                ) for participant_id in self.validated_data['participants']
            ]
            return QuizParticipant.objects.bulk_create(quiz_participants)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
