from django.contrib import admin
from clients import models, forms

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    
    

    list_display = ('id', 'first_name','last_name','email','phone','mobile', 'company_name','is_client')

    list_filter = ('first_name', 'company_name', 'is_client')
