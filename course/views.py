from rest_framework.views import View
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
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


class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListCreateSerializer


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetrieveUpdateDestroySerializer
    lookup_field = 'pk'