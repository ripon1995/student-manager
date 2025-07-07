from django.urls import path
from course.views.api_views import CourseListCreateAPIView, CourseRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view(), name="course_list_create_api"),
    path('course/<uuid:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name="course_detail_update_delete_api"),
]
