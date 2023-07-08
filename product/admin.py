from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

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
class FeatureInline(admin.TabularInline):
    model = models.ProductFeature
    extra = 2


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # Product List in Admin
    list_display = ['pk', 'title', 'get_description', 'price', 'off', 'get_image', ]
    list_display_links = ['title', 'pk']
    list_editable = ['off', ]

    list_filter = [PriceFilter]
    search_fields = ['title', ]
    ordering = ['pk', ]
    sortable_by = ['price', 'off']

    actions_on_bottom = True
    empty_value_display = 'NONE'

    def get_description(self, obj):
        return obj.description[:30] + '...' if len(obj.description) > 30 else obj.description

    get_description.short_description = _('description')

    # Editing Page in Admin
    readonly_fields = ['pk', 'get_image']
    fieldsets = (
        (_('Product detail'), {
            'fields': ('pk', 'title', 'description', 'get_image', 'image')
        }),
        (_('Price'), {
            'fields': ('price', 'off',)
        }),
        (_('Info'), {
            'fields': ('color', 'size',)
        }),
    )
    inlines = [FeatureInline]
    save_on_top = True

    def get_image(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100px" height="100x">')
        return self.empty_value_display

    get_image.short_description = _('image')


@admin.register(models.ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ['title']


class IsParentListFilter(admin.SimpleListFilter):
    title = _('Parent Filter')
    parameter_name = 'parent'

    def lookups(self, request, model_admin):
        return (
            ('0', _('Sub Categories')),
            ('1', _('Parent Categories')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(parent__in=queryset.all())

        if self.value() == '1':
            return queryset.exclude(parent__in=queryset.all())


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_filter = (IsParentListFilter,)


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
    ordering = ('-created_at',)


admin.site.register(models.Color)
admin.site.register(models.Size)
