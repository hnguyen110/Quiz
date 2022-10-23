from rest_framework.serializers import ModelSerializer

from quiz_app.models.quiz import Quiz


class BaseQuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'price']

    def create(self, validated_data):
        owner = self.context['owner']
        return Quiz.objects.create(owner=owner, **validated_data)
