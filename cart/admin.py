from django.contrib import admin

from .models import Order, OrderItem


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list page
    list_display = ['pk', 'user', 'is_paid']
    list_display_links = ['pk', ]
    list_editable = ['is_paid', ]
    list_filter = ['is_paid', ]
    actions_on_bottom = True
    actions_on_top = False

    # edit page
    inlines = [OrderItemInline, ]
    save_on_top = True


admin.site.register(OrderItem)
