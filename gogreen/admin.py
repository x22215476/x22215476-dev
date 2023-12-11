from django.contrib import admin
# Register your models here.
from .models import Plants
from .models import Order

admin.site.register(Plants)
admin.site.register(Order)
