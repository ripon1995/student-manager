from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from course.models import Course
from course.serializers import CourseListCreateSerializer, CourseRetrieveUpdateDestroySerializer
from student_manager.utils.custom_global_exceptions import InvalidUUIDException
from student_manager.utils.helper_methods import validate_uuid


class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListCreateSerializer


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetrieveUpdateDestroySerializer
    lookup_field = 'pk'

    def get_object(self):
        pk = self.kwargs.get(self.lookup_field)
        try:
            validate_uuid(pk)
        except Exception as e:
            raise InvalidUUIDException