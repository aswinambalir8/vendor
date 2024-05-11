from django.db import models
from django.db.models import Count, Avg, Sum
from datetime import timedelta
# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)

    def update_on_time_delivery_rate(self):
        completed_orders_count = self.purchaseorder_set.filter(status='completed').count()
        if completed_orders_count > 0:
            on_time_orders_count = self.purchaseorder_set.filter(status='completed',
                                                                 delivery_date__lte=models.F('delivery_date')).count()
            self.on_time_delivery_rate = (on_time_orders_count / completed_orders_count) * 100
            self.save()

    def update_quality_rating_avg(self):
        completed_orders = self.purchaseorder_set.filter(status='completed', quality_rating__isnull=False)
        if completed_orders.exists():
            self.quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg']
            self.save()

    def update_average_response_time(self):
        completed_orders = self.purchaseorder_set.filter(acknowledgment_date__isnull=False)
        response_times = [(order.acknowledgment_date - order.issue_date).total_seconds() / 3600 for order in
                          completed_orders if order.acknowledgment_date]
        if response_times:
            self.average_response_time = sum(response_times) / len(response_times)
            self.save()

    def update_fulfilment_rate(self):
        total_orders_count = self.purchaseorder_set.count()
        successful_orders_count = self.purchaseorder_set.filter(status='completed',
                                                                acknowledgment_date__isnull=False).count()
        if total_orders_count > 0:
            self.fulfillment_rate = (successful_orders_count / total_orders_count) * 100
            self.save()


def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.vendor.update_on_time_delivery_rate()
        self.vendor.update_quality_rating_avg()
        self.vendor.update_average_response_time()
        self.vendor.update_fulfilment_rate()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.vendor.update_on_time_delivery_rate()
        self.vendor.update_quality_rating_avg()
        self.vendor.update_average_response_time()
        self.vendor.update_fulfilment_rate()

    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"