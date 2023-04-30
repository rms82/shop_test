from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


class PriceFilter(admin.SimpleListFilter):
    title = _('Price')
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('cheap', _("Cheap")),
            ('expensive', _("expensive")),
        )

    def queryset(self, request, queryset):
        if self.value() == 'cheap':
            return queryset.filter(price__lt=150)

        elif self.value() == 'expensive':
            return queryset.filter(price__gte=150)


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # Product List in Admin
    list_display = ['pk', 'title', 'des', 'price', 'off', 'image', ]
    list_display_links = ['title', 'pk']
    list_editable = ['off', ]

    list_filter = [PriceFilter]
    search_fields = ['title', ]
    ordering = ['pk', ]
    sortable_by = ['price', 'off']

    actions_on_bottom = True
    empty_value_display = 'UNSET'

    def des(self, obj):
        return obj.description[:30] + '...' if len(obj.description) > 30 else obj.description

    des.short_description = _('description')

    # Editing Page in Admin
    readonly_fields = ['pk']
    fieldsets = (
        (_('Product detail'), {
            'fields': ('pk', 'title', 'description', 'image')
        }),
        (_('Price'), {
            'fields': ('price', 'off', )
        }),
        (_('Info'), {
            'fields': ('color', 'size',)
        }),
    )
    save_on_top = True


admin.site.register(models.Color)
admin.site.register(models.Size)
