from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from course.models import Course
from course.serializers import CourseListCreateSerializer, CourseRetrieveUpdateDestroySerializer


class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListCreateSerializer


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetrieveUpdateDestroySerializer
    lookup_field = 'pk'
