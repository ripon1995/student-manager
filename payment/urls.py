from django.urls import path
from .views import PaymentListCreateAPIView


urlpatterns = [
    path('payments/', PaymentListCreateAPIView.as_view(), name='payment_list_create_api_view'),
]