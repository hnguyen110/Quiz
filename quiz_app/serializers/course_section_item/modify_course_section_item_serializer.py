from rest_framework.serializers import ModelSerializer

from quiz_app.models.course_section_item import CourseSectionItem


class ModifyCourseSectionItemSerializer(ModelSerializer):
    class Meta:
        model = CourseSectionItem
        fields = ['id', 'order', 'title', 'data']

    def create(self, validated_data):
        data = validated_data['data']
        course_section_id = self.context['course_section_id']
        return CourseSectionItem \
            .objects \
            .create(course_section_id=course_section_id, size=data.size,
                    content_type=data.content_type, **validated_data)

    def update(self, instance, validated_data):
        instance.data.delete()
        return super(ModifyCourseSectionItemSerializer, self).update(instance, validated_data)
