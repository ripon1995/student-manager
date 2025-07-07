from django.urls import path
from student.views.api_views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student_list_create_api'),
    path('student/<uuid:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student_detail_update_delete_api'),
]
