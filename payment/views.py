import datetime
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Payment
from .serializers import PaymentListCreateSerializer, CurrentMonthPaymentListSerializer


class PaymentListCreateAPIView(ListCreateAPIView):
    serializer_class = PaymentListCreateSerializer
    queryset = Payment.objects.all()


class CurrentMonthPaymentListAPIView(ListAPIView):
    serializer_class = CurrentMonthPaymentListSerializer
    queryset = Payment.objects.all()

    def get_date_range(self):
        now = datetime.datetime.now()
        first_day = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        if now.month == 12:
            next_month = now.replace(year=now.year + 1, month=1, day=1)
        else:
            next_month = now.replace(month=now.month + 1, day=1)
        return first_day, next_month

    def get_queryset(self):
        course = self.request.query_params.get('course', None)
        first_day, next_month = self.get_date_range()
        return self.queryset.filter(course=course, date__gte=first_day, date__lt=next_month).order_by('date')
