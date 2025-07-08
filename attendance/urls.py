from django.urls import path
from .views import AttendanceBulkCreateAPIView, AttendanceListByCourseAPIView

urlpatterns = [
    path('api/attendances/', AttendanceBulkCreateAPIView.as_view(), name='attendance_bulk_create_api'),
    path('api/attendances/list/', AttendanceListByCourseAPIView.as_view(),
         name='attendance_list_by_course_and_date_api'),
]
