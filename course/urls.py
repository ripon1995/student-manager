from django.urls import path
from .views import CourseListCreateAPIView, CourseRetrieveUpdateDestroyAPIView
from .views import CourseListView

urlpatterns = [
    path('api/courses/', CourseListCreateAPIView.as_view(), name="course_list_create_api"),
    path("api/course/<uuid:pk>/", CourseRetrieveUpdateDestroyAPIView.as_view(), name="course_detail_update_delete_api"),
]

template_urls = [
    path('courses/', CourseListView.as_view(), name='course_list_view'),
]

urlpatterns += template_urls