from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from student.models import Student


class StudentListCreateSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'guardian_name', 'contact_number', 'guardian_contact_number',
                  'start_date']
        read_only_fields = ['id', 'start_date']


class StudentRetrieveUpdateDestroySerializer(ModelSerializer):
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    contact_number = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'guardian_name', 'contact_number', 'guardian_contact_number',
                  'start_date']
        read_only_fields = ['id']
