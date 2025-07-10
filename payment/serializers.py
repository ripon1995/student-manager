from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Payment


class PaymentListCreateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'payment_for_month', 'date', 'student', 'course']
        read_only_fields = ['date']  # Date should be set automatically on creation


class CurrentMonthPaymentListSerializer(ModelSerializer):
    student_name = serializers.CharField(source='student_full_name', read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'amount', 'payment_for_month', 'date', 'student_name', 'course']
        read_only_fields = ['date']  # Date should be set automatically on creation
