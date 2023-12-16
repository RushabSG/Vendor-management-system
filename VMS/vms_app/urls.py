from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('vendors', views.VendorView.as_view()),
    path('vendors/<int:pk>', views.SingleVendorView.as_view()),
    path('purchase_orders', views.PurchaseOrderView.as_view()),
    path('purchase_orders/<int:pk>', views.SinglePurchaseOrderView.as_view()),
    path('vendors/<int:pk>/performance', views.VendorPerformanceView.as_view()),
    path('purchase_orders/<int:pk>/acknowledge', views.AcknowledgeView.as_view()),
    path('api-token', obtain_auth_token),
]