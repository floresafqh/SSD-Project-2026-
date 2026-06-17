from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9 ]+$',
        message="Item name must contain only alphanumeric characters and spaces."
    )
    name = models.CharField(max_length=100, validators=[name_validator])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Added to fulfill Section 3.A.5 requirement
class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    user = models.CharField(max_length=150, default='System / Anonymous')
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"[{self.timestamp}] {self.user} - {self.action}"