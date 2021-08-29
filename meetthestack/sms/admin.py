from django.contrib import admin

from .models import SmsMessage


@admin.register(SmsMessage)
class SmsMessageAdmin(admin.ModelAdmin):
    search_fields = ('from_number', 'to_number', 'body', 'sid', 'related_user')
    list_display = ('date_created',
                    'from_number',
                    'to_number',
                    'body',
                    'related_user')
