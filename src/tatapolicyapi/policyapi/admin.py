from django.contrib import admin
from .models import data_policy
# Register your models here.

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('policy_no','policy_cname','policy_type','policy_status')

admin.site.register(data_policy,PolicyAdmin)