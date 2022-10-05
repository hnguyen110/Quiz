from rest_framework.serializers import ModelSerializer

from quiz_app.models.question import Question


class BaseQuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'type', 'description']

    def create(self, validated_data):
        quiz_id = self.context['quiz_id']
        return Question.objects.create(quiz_id=quiz_id, **validated_data)
