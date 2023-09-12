from django.contrib import admin

from api.models import LinkShortener

EMPTY_VALUE = '--NONE--'


@admin.register(LinkShortener)
class LinkShortener(admin.ModelAdmin):
    list_display = ('pk', 'short_link', 'link_to_shorten')
    search_fields = ('short_link', 'link_to_shorten', )
    empty_value_display = EMPTY_VALUE
