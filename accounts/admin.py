from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, OTP, Address
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.
class AddressInline(admin.StackedInline):
    model = Address
    extra = 0


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['phone', "fullname", "is_superuser"]
    list_filter = ["is_superuser"]
    fieldsets = [
        (None, {"fields": ['phone', "email", "password"]}),
        (_("Personal info"), {"fields": ["fullname"]}),
        (_("Permissions"), {"fields": ["is_superuser", 'is_staff', 'is_active']}),
        (_("Groups"), {"fields": ["user_permissions", 'groups']}),

    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ['phone', "email", "fullname", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["phone"]
    ordering = ["email"]
    filter_horizontal = []
    inlines = [AddressInline, ]


class OTPAdmin(admin.ModelAdmin):
    list_display = ['phone', 'otp']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'fullname', 'email']


# Now register the new UserAdmin...
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OTP, OTPAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)
