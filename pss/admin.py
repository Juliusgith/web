# pss/admin.py

from django.contrib import admin
from .models import Registration
from django.utils.safestring import mark_safe

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'membership_type', 'address', 'date_of_birth', 'phone_number', 'email', 'year_at_panyango', 'occupation', 'membership_fee', 'image_tag']
    search_fields = ('name', 'email')

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "No Image"

    image_tag.short_description = 'Image'

# admin.py

from django.contrib import admin
from .models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'date_created', 'month_created', 'year_created')
    list_filter = ('month_created', 'year_created')
    search_fields = ('name', 'email')

admin.site.register(Subscription, SubscriptionAdmin)
