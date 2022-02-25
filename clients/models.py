from django.db import models
# from accounts.models import User
from django.conf import settings


class Client(models.Model):

    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    email = models.EmailField(max_length=150,blank=False)
    phone = models.CharField(max_length=20,blank=False,default='xxxxxxxxxx')
    mobile = models.CharField(max_length=20,blank=False,default='xxxxxxxxxx')
    company_name = models.CharField(unique=True, max_length=250, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    is_client = models.BooleanField(default=False)
    # if is_client:
    sale_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        
        return f"{self.first_name} {self.last_name} {self.company_name}"