from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(BillProduct)

