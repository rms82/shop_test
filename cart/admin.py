from django.contrib import admin

from .models import Order, OrderItem, OffCode


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list page
    list_display = ['pk', 'user', 'total_price', 'is_paid']
    list_display_links = ['pk', ]
    list_editable = ['is_paid', ]
    list_filter = ['is_paid', ]
    ordering = ['pk']
    actions_on_bottom = True
    actions_on_top = False

    # edit page
    inlines = [OrderItemInline, ]
    save_on_top = True


@admin.register(OffCode)
class OrderAdmin(admin.ModelAdmin):
    # list page
    list_display = ['pk', 'code', 'off', 'quantity']
    list_display_links = ['pk', 'code']
    list_editable = ['quantity', ]
    ordering = ['pk']
    sortable_by = ['off', 'quantity']


admin.site.register(OrderItem)
