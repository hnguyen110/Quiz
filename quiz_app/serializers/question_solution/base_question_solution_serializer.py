from rest_framework.serializers import ModelSerializer

from quiz_app.models.question_solution import QuestionSolution


class BaseQuestionSolutionSerializer(ModelSerializer):
    class Meta:
        model = QuestionSolution
        fields = ['id', 'description', 'isCorrect']

    def create(self, validated_data):
        question_id = self.context['question_id']
        return QuestionSolution.objects.create(question_id=question_id, **validated_data)
