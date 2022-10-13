from rest_framework.serializers import ModelSerializer

from quiz_app.models.course import Course


class BaseCourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description']

    def create(self, validated_data):
        owner = self.context['owner']
        return Course.objects.create(owner=owner, **validated_data)
