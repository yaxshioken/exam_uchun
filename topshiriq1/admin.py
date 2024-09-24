from django.contrib import admin

from topshiriq1.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass
