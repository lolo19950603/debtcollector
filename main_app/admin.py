from msilib.schema import Patch
from django.contrib import admin

# Register your models here.
from .models import Debtor, Payment

# Register your models here
admin.site.register(Debtor)

admin.site.register(Payment)
