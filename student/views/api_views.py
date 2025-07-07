from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from student.models import Student
from student.serializers import StudentListCreateSerializer, StudentRetrieveUpdateDestroySerializer


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListCreateSerializer


class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRetrieveUpdateDestroySerializer
    lookup_field = 'pk'
