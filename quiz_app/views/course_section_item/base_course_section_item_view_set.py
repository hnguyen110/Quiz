from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.course_section_item import CourseSectionItem
from quiz_app.serializers.course_section_item.base_course_section_item_serializer import BaseCourseSectionItemSerializer
from quiz_app.serializers.course_section_item.modify_course_section_item_serializer import \
    ModifyCourseSectionItemSerializer
from utilities.permissions.is_course_participant import IsCourseParticipant


class BaseCourseSectionItemViewSet(ModelViewSet):
    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsCourseParticipant]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.is_staff:
            return CourseSectionItem \
                .objects \
                .filter(course_section_id=self.kwargs['section_pk'], course_section__course__owner=self.request.user)
        else:
            return CourseSectionItem.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BaseCourseSectionItemSerializer
        else:
            return ModifyCourseSectionItemSerializer

    def get_serializer_context(self):
        return {
            'course_section_id': self.kwargs['section_pk']
        }
