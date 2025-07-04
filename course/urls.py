from django.urls import path, include

urlpatterns = [
    path('api/', include('course.course_urls.api_urls')),
    path('view/', include('course.course_urls.template_urls')),
]
