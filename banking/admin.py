from django.contrib import admin
from .models import CustomUser, KYC

admin.site.register(CustomUser)
admin.site.register(KYC)
