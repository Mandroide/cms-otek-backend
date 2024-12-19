from rest_framework import viewsets

from .models import CustomerModel, AddressModel
from .serializers import AddressSerializer, CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = AddressModel.objects.all()
    serializer_class = AddressSerializer
