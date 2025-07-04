from rest_framework.serializers import ModelSerializer
from course.models import Course


class CourseListCreateSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "description", "created_at"]
        read_only_fields = ["created_at"]
