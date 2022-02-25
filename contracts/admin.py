from django.contrib import admin
from contracts import models

@admin.register(models.Contract)
class ClientAdmin(admin.ModelAdmin):
    

    list_display = ("id", "sales_contact", "client", "date_created", "date_updated", "status", "amount")

    list_filter = ("client", "sales_contact", "status")