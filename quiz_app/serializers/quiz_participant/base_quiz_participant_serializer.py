from rest_framework.serializers import ModelSerializer

from quiz_app.models.quiz_participant import QuizParticipant


class BaseQuizParticipantSerializer(ModelSerializer):
    class Meta:
        model = QuizParticipant
        fields = ['id', 'user', 'quiz', 'isComplete']

    def create(self, validated_data):
        quiz_id = self.context['quiz_id']
        return QuizParticipant.objects.create(quiz_id=quiz_id, **validated_data)
