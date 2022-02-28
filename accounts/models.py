from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):

    MANAGEMENT = "MANAGEMENT"
    SALE = "SALE"
    SUPPORT = "SUPPORT"

    USER_TYPE_CHOICES = (
        (MANAGEMENT, "Management"),
        (SALE, "sale"),
        (SUPPORT, "support"),
    )

    user_type = models.CharField(
        max_length=30,
        choices=USER_TYPE_CHOICES,
        verbose_name="role",
        default=MANAGEMENT,
    )
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(verbose_name="is_staff", default=True)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        if self.user_type == self.MANAGEMENT:
            group = Group.objects.get(name="MANAGEMENT")
            group.user_set.add(self)

        elif self.user_type == self.SALE:
            group = Group.objects.get(name="SALE")
            group.user_set.add(self)

        elif self.user_type == self.SUPPORT:
            group = Group.objects.get(name="SUPPORT")
            group.user_set.add(self)
