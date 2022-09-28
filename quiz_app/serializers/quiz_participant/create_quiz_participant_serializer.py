from rest_framework.serializers import ModelSerializer

from quiz_app.models.quiz_participant import QuizParticipant


class CreateQuizParticipantSerializer(ModelSerializer):
    class Meta:
        model = QuizParticipant
        fields = ['id', 'user', 'isComplete']
