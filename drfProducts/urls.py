from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls')),
    path('bill-product/', views.bill_product_list),
    path('bill-product/<int:pk>/', views.bill_product_detail),
    path('bill-product/csv/<int:pk>/', views.BillProductCSVExport)
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', ])