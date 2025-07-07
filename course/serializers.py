from rest_framework.serializers import ModelSerializer
from course.models import Course


class CourseListCreateSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "description", "created_at"]
        read_only_fields = ["created_at"]


class CourseRetrieveUpdateDestroySerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "description", "created_at", "students"]
        read_only_fields = ["title", "created_at"]
