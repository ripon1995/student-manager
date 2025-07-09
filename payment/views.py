from rest_framework.generics import ListCreateAPIView
from .models import Payment
from .serializers import PaymentListCreateSerializer


class PaymentListCreateAPIView(ListCreateAPIView):
    serializer_class = PaymentListCreateSerializer
    queryset = Payment.objects.all()
