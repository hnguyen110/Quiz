from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.course import Course
from quiz_app.models.course_participant import CourseParticipant
from quiz_app.serializers.course.assigned_course_details_serializer import AssignedCourseDetailsSerializer
from quiz_app.serializers.course.base_course_serializer import BaseCourseSerializer
from quiz_app.serializers.course_participant.base_course_participant_with_details_serializer import \
    BaseCourseParticipantWithDetailsSerializer
from quiz_app.serializers.course_participant.modify_course_participant_serializer import \
    ModifyCourseParticipantSerializer
from quiz_app.serializers.course_participant.modify_course_participants_serializer import \
    ModifyCourseParticipantsSerializer
from quiz_app.serializers.stripe.base_payment_serializer import BasePaymentSerializer
from utilities.permissions.is_course_participant import IsCourseParticipant


class BaseCourseViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'assign_participants':
            return ModifyCourseParticipantsSerializer
        elif self.action == 'checkout':
            return BasePaymentSerializer
        else:
            return BaseCourseSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsCourseParticipant]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'get_assigned_courses':
            permission_classes = [IsAuthenticated]
        elif self.action == 'get_assigned_course_details':
            permission_classes = [IsCourseParticipant]
        elif self.action == 'checkout':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Course.objects.filter(owner=self.request.user)
        else:
            return Course.objects.exclude(participants__user=self.request.user)

    def get_serializer_context(self):
        return {
            'owner': self.request.user
        }

    @action(detail=False, methods=['get'], url_path='assigned-courses')
    def get_assigned_courses(self, request, **kwargs):
        queryset = CourseParticipant.objects.filter(user=self.request.user)
        serializer = BaseCourseParticipantWithDetailsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='assigned-course-details')
    def get_assigned_course_details(self, request, **kwargs):
        course = get_object_or_404(
            Course
            .objects
            .filter(participants__user=self.request.user)
            .prefetch_related('sections__items'), pk=kwargs['pk']
        )
        serializer = AssignedCourseDetailsSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='assign-participants')
    def assign_participants(self, request, **kwargs):
        serializer = ModifyCourseParticipantsSerializer(
            data=request.data,
            context={
                'course_id': kwargs['pk']
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='checkout')
    def checkout(self, request, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'])
        payment_serializer = BasePaymentSerializer(data=request.data, context={
            'name': self.request.user.email,
            'email': self.request.user.email,
            'amount': int(course.price) * 100,
            'currency': 'usd',
            'description': course.title
        })
        payment_serializer.is_valid(raise_exception=True)
        payment_serializer.save()
        participant_serializer = ModifyCourseParticipantSerializer(data={
            'user': self.request.user.pk,
        }, context={
            'course_id': course.pk
        })
        participant_serializer.is_valid(raise_exception=True)
        participant_serializer.save()
        return Response(participant_serializer.data, status=status.HTTP_200_OK)
