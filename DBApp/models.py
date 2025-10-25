from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    # Fix reverse accessor conflicts by giving unique related_name
    groups = models.ManyToManyField(
        Group,
        related_name="banking_customuser_set",  # unique for this app
        blank=True,
        help_text=("The groups this user belongs to."),
        verbose_name=("groups"),
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="banking_customuser_set_permissions",  # unique for this app
        blank=True,
        help_text=("Specific permissions for this user."),
        verbose_name=("user permissions"),
    )

    def __str__(self):
        return self.username
