from django.contrib import admin

# Register your models here.
from .models import Debtor, Payment, Insurance

# Register your models here
admin.site.register(Debtor)

admin.site.register(Payment)

admin.site.register(Insurance)
