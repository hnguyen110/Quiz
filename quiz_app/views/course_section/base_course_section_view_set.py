from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.course_section import CourseSection
from quiz_app.serializers.course_section_serializer.base_course_section_serializer import BaseCourseSectionSerializer


class BaseCourseSectionViewSet(ModelViewSet):
    serializer_class = BaseCourseSectionSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return CourseSection.objects.filter(course_id=self.kwargs['course_pk'])

    def get_serializer_context(self):
        return {
            'course_id': self.kwargs['course_pk']
        }
