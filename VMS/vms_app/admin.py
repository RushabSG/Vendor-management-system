from django.contrib import admin
from vms_app.models import VendorModel, PurchaseOrderModel, HistroicalPerfomanceModel
# Register your models here.

admin.site.register(VendorModel)
admin.site.register(PurchaseOrderModel)
admin.site.register(HistroicalPerfomanceModel)