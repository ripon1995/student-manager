from django.urls import path
from .views import PaymentListCreateAPIView, CurrentMonthPaymentListAPIView


urlpatterns = [
    path('payments/', PaymentListCreateAPIView.as_view(), name='payment_list_create_api_view'),
    path('payments/current-month/', CurrentMonthPaymentListAPIView.as_view(), name='current_month_payment_list_api_view'),
]