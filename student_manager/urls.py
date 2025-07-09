
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    path('course/', include('course.urls')),

    path('student/', include('student.urls')),

    path('attendance/', include('attendance.urls')),

    path('payment/api/', include('payment.urls')),
]
