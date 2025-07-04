from django.urls import path
from .views import CourseListCreateAPIView
from .views import CourseListView

urlpatterns = [
    path('api/courses/', CourseListCreateAPIView.as_view(), name="course_list_create"),
    # path("courses/<int:pk>/", CourseRetrieveUpdateDestroyAPIView.as_view(), name="course_detail"),
    # path("students/", StudentListCreateAPIView.as_view(), name="student_list_create"),
    # path("students/<int:pk>/", StudentRetrieveUpdateDestroyAPIView.as_view(), name="student_detail"),
]

template_urls = [
    path('courses/', CourseListView.as_view(), name='course_list_view'),
]

urlpatterns += template_urls