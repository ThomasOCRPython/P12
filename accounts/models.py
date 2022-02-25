from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    MANAGEMENT = 'MANAGEMENT'
    SALE = 'SALE'
    SUPPORT = 'SUPPORT'

    USER_TYPE_CHOICES = (
      (MANAGEMENT, 'Management'),
      (SALE, 'sale'),
      (SUPPORT, 'support'),
    )

    user_type = models.CharField(max_length=30,choices=USER_TYPE_CHOICES,verbose_name='role',default=MANAGEMENT)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)

    
