from django.shortcuts import render
from vms_app.models import VendorModel, PurchaseOrderModel, HistroicalPerfomanceModel
from . import serializers
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class VendorView(generics.ListCreateAPIView):
    serializer_class = serializers.VendorSerializer
    queryset = VendorModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class SingleVendorView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.VendorSerializer
    queryset = VendorModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PurchaseOrderView(generics.ListCreateAPIView):
    serializer_class = serializers.PurchaseOrderSerializer
    queryset = PurchaseOrderModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = PurchaseOrderModel.objects.all()
        vendor_id = self.request.query_params.get('vendor')
        if vendor_id is not None:
            queryset = queryset.filter(vendor__name=vendor_id)
        return queryset
    

class SinglePurchaseOrderView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PurchaseOrderSerializer
    queryset = PurchaseOrderModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class VendorPerformanceView(generics.RetrieveAPIView):
    serializer_class = serializers.VendorPerformanceSerializer
    queryset = VendorModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class AcknowledgeView(generics.UpdateAPIView):
    serializer_class = serializers.AcknowledgeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # queryset = PurchaseOrderModel.objects.all()

    def get_queryset(self):
        pk = self.kwargs['pk']
        return PurchaseOrderModel.objects.filter(id=pk)
