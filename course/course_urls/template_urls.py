from django.urls import path
from course.views.template_views import CourseListView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course_list_view'),
    path('course/<pk>/', CourseDetailView.as_view(), name='course_detail_view'),
]