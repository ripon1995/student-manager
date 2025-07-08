from .serializers import AttendanceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView


class AttendanceBulkCreateAPIView(CreateAPIView):
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        course = request.data.get('course')
        date = request.data.get('date')
        students = request.data.get('students', [])
        print('student : ', students)
        print('course', course)
        print('date', date)
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
