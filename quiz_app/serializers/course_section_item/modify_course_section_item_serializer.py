from uuid import uuid4

from rest_framework.serializers import ModelSerializer

from quiz_app.models.course_section_item import CourseSectionItem


class ModifyCourseSectionItemSerializer(ModelSerializer):
    class Meta:
        model = CourseSectionItem
        fields = ['id', 'order', 'title', 'data']

    def create(self, validated_data):
        data = validated_data['data']
        validated_data['data'].name = uuid4().hex
        course_section_id = self.context['course_section_id']
        return CourseSectionItem \
            .objects \
            .create(course_section_id=course_section_id,
                    size=data.size if data is not None else 0,
                    content_type=data.content_type if data is not None else None,
                    **validated_data)

    def update(self, instance, validated_data):
        data = validated_data['data'] if 'data' in validated_data else None
        if data is not None:
            instance.data.delete()
            instance.size = data.size
            instance.content_type = data.content_type
            validated_data['data'].name = uuid4().hex
        else:
            validated_data['data'] = instance.data
        return super(ModifyCourseSectionItemSerializer, self).update(instance, validated_data)
