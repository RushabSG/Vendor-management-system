from rest_framework import serializers
from vms_app.models import VendorModel, PurchaseOrderModel, HistroicalPerfomanceModel

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = "__all__"

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderModel
        fields = "__all__"

class HistoryPerformanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = HistroicalPerfomanceModel
        fields = "__all__"

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = [
            'on_time_delivery_rate',
            'quality_rating_avg',
            'average_response_time',
            'fulfillment_rate',
        ]

class AcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderModel
        fields = [
            'acknowledgment_date'
        ]
