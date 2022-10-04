from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.quiz import Quiz
from quiz_app.serializers.quiz.base_quiz_serializer import BaseQuizSerializer


class BaseQuizViewSet(ModelViewSet):
    serializer_class = BaseQuizSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Quiz.objects.filter(owner=self.request.user)

    def get_serializer_context(self):
        return {
            'owner': self.request.user
        }

    @action(detail=False, methods=['get'], url_path='assigned-quizzes', permission_classes=[IsAuthenticated])
    def get_assigned_quizzes(self, request, **kwargs):
        queryset = Quiz \
            .objects \
            .filter(participants__user=self.request.user, participants__isComplete=False)
        serializer = BaseQuizSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
