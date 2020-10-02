from django.contrib import admin
from .models import Account, Guide

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')


admin.site.register(Account, AccountAdmin)


class GuideAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


admin.site.register(Guide, GuideAdmin)
