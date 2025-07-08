from django.urls import path
from .views import AttendanceBulkCreateAPIView

urlpatterns = [
    path('api/attendances/', AttendanceBulkCreateAPIView.as_view(), name='attendance_bulk_create_api'),
]
