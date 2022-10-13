from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.course import Course
from quiz_app.serializers.course.base_course_serializer import BaseCourseSerializer


class BaseCourseViewSet(ModelViewSet):
    serializer_class = BaseCourseSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)

    def get_serializer_context(self):
        return {
            'owner': self.request.user
        }
