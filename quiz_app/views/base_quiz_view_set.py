from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.quiz import Quiz
from quiz_app.serializers.base_quiz_serializer import BaseQuizSerializer


class BaseQuizViewSet(ModelViewSet):
    serializer_class = BaseQuizSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Quiz.objects.filter(owner=self.request.user)

    def get_serializer_context(self):
        return {
            'owner': self.request.user
        }
