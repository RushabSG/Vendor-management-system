from typing import Iterable, Optional
from django.db import models
from django.utils import timezone
from django.db.models import F, Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class VendorModel(models.Model):

    name = models.CharField(max_length=100)  # CharField - Vendor's name.
    # TextField - Contact information of the vendor.
    contact_details = models.TextField()
    address = models.TextField()  # TextField - Physical address of the vendor.
    # CharField - A unique identifier for the vendor.
    vendor_code = models.CharField(max_length=50, unique=True)
    # FloatField - Tracks the percentage of on-time deliveries.
    on_time_delivery_rate = models.FloatField(default=0.0)
    # FloatField - Average rating of quality based on purchase orders.
    quality_rating_avg = models.FloatField(default=0.0)
    # FloatField - Average time taken to acknowledge purchase orders.
    average_response_time = models.FloatField(default=0.0)
    # FloatField - Percentage of purchase orders fulfilled successfully.
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.name

    def calculate_on_time_delivery_rate(self):
        completed_pos = self.purchaseordermodel_set.filter(status='completed')
        total_completed_pos = completed_pos.count()
        on_time_deliveries = completed_pos.filter(
            delivery_date__lte=timezone.now()).count()
        on_time_delivery_rate = (
            on_time_deliveries/total_completed_pos) * 100 if total_completed_pos > 0 else 0
        return on_time_delivery_rate

    def calculate_quality_rating_avg(self):
        completed_pos_with_rating = self.purchaseordermodel_set.filter(
            status='completed', quality_rating__isnull=False)
        avg_rating = completed_pos_with_rating.aggregate(
            avg_rating=Avg('quality_rating'))['avg_rating']
        return avg_rating or 0

    def calculate_average_response_time(self):
        acknowledged_pos = self.purchaseordermodel_set.filter(
            status='completed', acknowledgment_date__isnull=False)

        response_times = acknowledged_pos.annotate(response_time=F('acknowledgment_date') - F('issue_date'))
        return response_times.aggregate(Avg('response_time'))['response_time__avg'].total_seconds() or 0

    def calculate_fulfillment_rate(self):
        total_pos = self.purchaseordermodel_set.count()
        completed_pos_without_issues = self.purchaseordermodel_set.filter(
            status='completed', quality_rating__isnull=False).count()
        return (completed_pos_without_issues / total_pos) * 100 if completed_pos_without_issues <= total_pos else 100.0


class PurchaseOrderModel(models.Model):

    # CharField - Unique number identifying the PO.
    po_number = models.CharField(max_length=50, unique=True)
    # ForeignKey - Link to the Vendor model.
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    # DateTimeField - Date when the order was placed.
    order_date = models.DateTimeField()
    # DateTimeField - Expected or actual delivery date of the order.
    delivery_date = models.DateTimeField()
    items = models.JSONField()  # JSONField - Details of items ordered.
    # IntegerField - Total quantity of items in the PO.
    quantity = models.IntegerField()
    status_choice = [
        ('pending', 'pending'),
        ('completed', 'completed'),
        ('canceled', 'canceled'),
    ]
    # CharField - Current status of the PO (e.g., pending, completed, canceled).
    status = models.CharField(
        max_length=10, choices=status_choice, default='pending')
    # FloatField - Rating given to the vendor for this PO (nullable).
    quality_rating = models.FloatField(null=True, blank=True)
    # DateTimeField - Timestamp when the PO was issued to the vendor.
    issue_date = models.DateTimeField()
    # DateTimeField, nullable - Timestamp when the vendor acknowledged the PO.
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.po_number + ' - ' + self.vendor.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == 'completed' and self.delivery_date <= timezone.now():
            self.vendor.on_time_delivery_rate = self.vendor.calculate_on_time_delivery_rate()
            self.vendor.save()

        if self.quality_rating is not None:
            self.vendor.quality_rating_avg = self.vendor.calculate_quality_rating_avg()
            self.vendor.save()

        if self.acknowledgment_date is not None:
            self.vendor.average_response_time = self.vendor.calculate_average_response_time()
            self.vendor.save()

        if self.status == 'completed':
            self.vendor.fulfillment_rate = self.vendor.calculate_fulfillment_rate()
            self.vendor.save()


class HistroicalPerfomanceModel(models.Model):

    # ForeignKey - Link to the Vendor model.
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    # DateTimeField - Date of the performance record.
    date = models.DateTimeField()
    # FloatField - Historical record of the on-time delivery rate.
    on_time_delivery_rate = models.FloatField()
    # FloatField - Historical record of the quality rating average.
    quality_rating_avg = models.FloatField()
    # FloatField - Historical record of the average response time.
    average_response_time = models.FloatField()
    # FloatField - Historical record of the fulfilment rate.
    fulfillment_rate = models.FloatField()

    def __str__(self) -> str:
        return f'{self.vendor} - {self.date}'

@receiver(post_save, sender=PurchaseOrderModel)
def create_historical_performance(sender, instance, created, **kwargs):
    if instance.status == 'completed' and created:
        vendor = instance.vendor
        HistroicalPerfomanceModel.objects.create(
            vendor=vendor,
            date=instance.delivery_date,
            on_time_delivery_rate=vendor.on_time_delivery_rate,
            quality_rating_avg=vendor.quality_rating_avg,
            average_response_time=vendor.average_response_time,
            fulfillment_rate=vendor.fulfillment_rate,
        )