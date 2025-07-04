from django.urls import path
from course.views.template_views import CourseListView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course_list_view'),
]