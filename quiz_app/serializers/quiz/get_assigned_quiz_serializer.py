from rest_framework.serializers import ModelSerializer

from quiz_app.models.quiz import Quiz


class GetAssignedQuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'price', 'participants']
