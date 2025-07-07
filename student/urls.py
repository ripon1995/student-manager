from django.urls import path, include

urlpatterns = [
    path('api/', include('student.student_urls.api_urls')),
    # path('view/', include('student.student_urls.template_urls')),
]