from rest_framework.views import APIView, View
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from .models import Course
from .serializers import CourseListCreateSerializer, CourseRetrieveUpdateDestroySerializer


class CourseListView(View):
    template_name = 'course/course_list.html'

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        return render(request, self.template_name, {'courses': courses})


class CourseListCreateAPIView(APIView):
    serializer_class = CourseListCreateSerializer

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer = self.serializer_class(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetrieveUpdateDestroySerializer
    lookup_field = 'pk'