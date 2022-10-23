from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.quiz import Quiz
from quiz_app.models.quiz_participant import QuizParticipant
from quiz_app.serializers.quiz.base_quiz_serializer import BaseQuizSerializer
from quiz_app.serializers.quiz.get_assigned_quiz_details_serializer import GetAssignedQuizDetailsSerializer
from quiz_app.serializers.quiz_participant.base_quiz_participant_with_details_serializer import \
    BaseQuizParticipantWithDetailsSerializer
from quiz_app.serializers.quiz_participant.create_quiz_participant_serializer import CreateQuizParticipantSerializer
from quiz_app.serializers.stripe.base_payment_serializer import BasePaymentSerializer


class BaseQuizViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'checkout':
            return BasePaymentSerializer
        else:
            return BaseQuizSerializer

    def get_permissions(self):
        if self.action == 'checkout':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Quiz.objects.filter(owner=self.request.user)

    def get_serializer_context(self):
        return {
            'owner': self.request.user
        }

    @action(detail=False, methods=['get'], url_path='assigned-quizzes', permission_classes=[IsAuthenticated])
    def get_assigned_quizzes(self, request, **kwargs):
        queryset = QuizParticipant.objects.filter(user=self.request.user, isComplete=False)
        serializer = BaseQuizParticipantWithDetailsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # queryset = Quiz \
        #     .objects \
        #     .filter(participants__user=self.request.user, participants__isComplete=False) \
        #     .prefetch_related(Prefetch('participants',
        #                                queryset=QuizParticipant
        #                                .objects
        #                                .filter(user=self.request.user)))
        # serializer = GetAssignedQuizSerializer(queryset, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='assigned-quiz-details', permission_classes=[IsAuthenticated])
    def get_assigned_quiz_details(self, request, **kwargs):
        quiz = get_object_or_404(
            Quiz
            .objects
            .filter(participants__user=self.request.user, participants__isComplete=False)
            .prefetch_related('questions__solutions'), pk=kwargs['pk']
        )
        serializer = GetAssignedQuizDetailsSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='submitted-quizzes', permission_classes=[IsAuthenticated])
    def get_submitted_quizzes(self, request, **kwargs):
        queryset = QuizParticipant.objects.filter(user=self.request.user, isComplete=True)
        serializer = BaseQuizParticipantWithDetailsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='checkout')
    def checkout(self, request, **kwargs):
        quiz = get_object_or_404(Quiz, pk=kwargs['pk'])
        payment_serializer = BasePaymentSerializer(data=request.data, context={
            'name': self.request.user.email,
            'email': self.request.user.email,
            'amount': int(quiz.price) * 100,
            'currency': 'usd',
            'description': quiz.title
        })
        payment_serializer.is_valid(raise_exception=True)
        payment_serializer.save()
        participant_serializer = CreateQuizParticipantSerializer(data={
            'user': self.request.user.pk,
            'quiz': kwargs['pk']
        })
        participant_serializer.is_valid(raise_exception=True)
        participant_serializer.save()
        return Response(participant_serializer.data, status=status.HTTP_200_OK)
