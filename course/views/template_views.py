from rest_framework.views import View
from django.shortcuts import render
from course.models import Course


class CourseListView(View):
    template_name = 'course/course_list.html'

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        return render(request, self.template_name, {'courses': courses})
