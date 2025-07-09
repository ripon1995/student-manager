from rest_framework.serializers import ModelSerializer
from .models import Payment

class PaymentListCreateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'payment_for_month', 'date', 'student', 'course']
        read_only_fields = ['date']  # Date should be set automatically on creation



class CurrentMonthPaymentListSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'payment_for_month', 'date', 'student', 'course']
        read_only_fields = ['date']  # Date should be set automatically on creation