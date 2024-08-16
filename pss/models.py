import logging
from django.db import models

logger = logging.getLogger(__name__)

class Registration(models.Model):
    MEMBERSHIP_CHOICES = [
        ('Ordinary', 'Ordinary Membership'),
        ('Premium', 'Premium Membership'),
        ('Vip', 'VIP Membership'),
        ('Gold', 'Gold Membership'),
    ]

    name = models.CharField(max_length=100)
    membership_type = models.CharField(max_length=50, choices=MEMBERSHIP_CHOICES)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    year_at_panyango = models.CharField(max_length=9)
    occupation = models.CharField(max_length=100)
    membership_fee = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='register_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        logger.info(f"Saving registration for {self.name}")
        if self.image:
            logger.info(f"Image: {self.image}")
        else:
            logger.info("No image uploaded")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# models.py

from django.db import models
from django.utils import timezone

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    month_created = models.PositiveIntegerField(editable=False)
    year_created = models.PositiveIntegerField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.month_created = timezone.now().month
            self.year_created = timezone.now().year
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
