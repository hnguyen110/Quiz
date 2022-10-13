from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.course import Course
from quiz_app.serializers.course.base_course_serializer import BaseCourseSerializer
from utilities.permissions.is_course_participant import IsCourseParticipant


class BaseCourseViewSet(ModelViewSet):
    serializer_class = BaseCourseSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsCourseParticipant]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Course.objects.filter(owner=self.request.user)
        else:
            return Course.objects.all()

    def get_serializer_context(self):
        return {
            'owner': self.request.user
        }
