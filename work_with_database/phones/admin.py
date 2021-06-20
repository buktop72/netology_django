from django.contrib import admin
from phones.models import Phone

class PhonesAdmin(admin.ModelAdmin):
    ...


admin.site.register(Phone, PhonesAdmin)