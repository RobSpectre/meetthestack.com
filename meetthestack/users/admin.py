from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('phone_number',
                     'email')
    list_display = ('email',
                    'phone_number',
                    'score',
                    'date_joined',
                    'last_updated_on')
