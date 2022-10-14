from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from quiz_app.models.course_section_item import CourseSectionItem
from quiz_app.serializers.course_section_item.base_course_section_item_serializer import BaseCourseSectionItemSerializer
from quiz_app.serializers.course_section_item.modify_course_section_item_serializer import \
    ModifyCourseSectionItemSerializer


class BaseCourseSectionItemViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return CourseSectionItem \
            .objects \
            .filter(course_section_id=self.kwargs['section_pk'], course_section__course__owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BaseCourseSectionItemSerializer
        else:
            return ModifyCourseSectionItemSerializer

    def get_serializer_context(self):
        return {
            'course_section_id': self.kwargs['section_pk']
        }
