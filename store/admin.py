from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(orderItem)
admin.site.register(shippingAddress)