from django.contrib import admin

from .models import (
    Item,
    Order,
    Discount,
    Tax,
)


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description', 'price',
    )
    list_display_links = (
        'id', 'name',
    )
    search_fields = (
        'id', 'name',
    )
    list_editable = (
        'price',
    )
    save_on_top = True


admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(Discount)
admin.site.register(Tax)
