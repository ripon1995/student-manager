from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from course.models import Course


class CourseListCreateSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "description", "created_at"]
        read_only_fields = ["created_at"]


class CourseRetrieveUpdateDestroySerializer(ModelSerializer):
    days = serializers.CharField(required=False, allow_blank=True)
    time = serializers.CharField(required=False, allow_blank=True)
    course_quote = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Course
        fields = ["id", "title", "description", "created_at", "students", 'course_fee', "days", "time", "capacity", "course_quote"]
        read_only_fields = ["title", "created_at"]
