from rest_framework.serializers import ModelSerializer

from quiz_app.models.course_section import CourseSection


class BaseCourseSectionSerializer(ModelSerializer):
    class Meta:
        model = CourseSection
        fields = ['id', 'title']

    def create(self, validated_data):
        course_id = self.context['course_id']
        return CourseSection.objects.create(course_id=course_id, **validated_data)
