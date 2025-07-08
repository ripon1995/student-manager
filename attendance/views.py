from .serializers import AttendanceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .models import Attendance

class AttendanceBulkCreateAPIView(CreateAPIView):
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        course = request.data.get('course')
        date = request.data.get('date')
        students = request.data.get('students', [])
        created = []
        for student in students:
            data = {
                'student': student,
                'course': course,
                'date': date
            }
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            created.append(serializer.data)
        return Response(created, status=status.HTTP_201_CREATED)


class AttendanceListByCourseAPIView(APIView):
    serializer_class = AttendanceSerializer

    def post(self, request, *args, **kwargs):
        course_id = request.data.get('course')
        date = request.data.get('date')
        queryset = Attendance.objects.filter(course_id=course_id, date=date)
        serializer = AttendanceSerializer(queryset, many=True)
        return Response(serializer.data)

