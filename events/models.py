from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from contracts.models import Contract
from clients.models import Client
from django.conf import settings


class EventStatus(models.Model):

    STATUS_CHOICES = [
        ("0", "canceled"),
        ("1", "new event"),
        ("2", "in progress"),
        ("3", "finished"),
    ]

    event_status = models.CharField(choices=STATUS_CHOICES, max_length=30)

    def __str__(self):
        return self.event_status


class Event(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    contract = models.ForeignKey(Contract, on_delete=CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=RESTRICT, null=True
    )
    event_status = models.ForeignKey(EventStatus, on_delete=RESTRICT)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=500)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.client} {self.event_status} {self.notes}"
