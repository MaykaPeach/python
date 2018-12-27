from django.contrib import admin
from .models import User, Purchase, JointPurchase

# Register your models here.
# Register your models here.
admin.site.register([User, Purchase, JointPurchase])