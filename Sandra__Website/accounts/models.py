from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Các trường khác của bạn
    # ...

    # Thêm related_name để giải quyết lỗi xung đột
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Tên related_name mới
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Tên related_name mới
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )