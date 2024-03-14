from django.contrib import admin
from .models import FreeShortedUrls, FreeGeneratedQR

@admin.register(FreeShortedUrls)
class FreeShortedUrls(admin.ModelAdmin):
    list_display = ['destination_url', 'url_in_db', 'added', 'ttl', 'dead_link_time']
    list_filter = ['url_in_db', 'added', 'ttl']
    date_hierarchy = 'added'


@admin.register(FreeGeneratedQR)
class FreeGeneratedQR(admin.ModelAdmin):
    list_display = ['destination_url', 'url_in_db', 'added', 'ttl', 'dead_link_time']
    list_filter = ['url_in_db', 'added', 'ttl']
    date_hierarchy = 'added'