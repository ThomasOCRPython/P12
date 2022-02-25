from django.db import models
from accounts.models import User
from clients.models import Client
from django.conf import settings
from django.db.models.deletion import RESTRICT


class Contract(models.Model):

    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=RESTRICT, blank=True, null=True)
    client = models.ForeignKey(Client,on_delete=RESTRICT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.id} {self.client.company_name}"