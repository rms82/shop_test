from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.core import validators
from django.utils.translation import gettext_lazy as _


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['email', 'fullname']
#
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['email', 'fullname']


# Validators
def valid_phone(phone):
    if phone[0] != '0':
        raise ValidationError(
            _('Phone Number should start with 0'),
            code='start_with_0'
        )

    elif len(phone) != 11:
        raise ValidationError(
            _('Phone Number should be 11 numbers'),
            code='len_phone'
        )

    elif not phone.isnumeric():
        raise ValidationError(
            _('Phone Number must be all numbers')
        )

    return phone


def valid_password(password):
    if len(password) <= 6:
        raise ValidationError(
            _('Password must be  more than 6 character'),
            code='len_password'
        )
    elif password.isnumeric():
        raise ValidationError(
            _('Password must not be all numbers')
        )

    return password


# forms
class CustomUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = ["phone", "email", 'fullname']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Passwords don't match"))
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ["phone", 'email', "password", "fullname", "is_active", "is_admin"]


class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(), validators=[valid_phone])
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(), validators=[valid_phone])


class OTPForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(), validators=[validators.MaxLengthValidator(4)])
    password = forms.CharField(widget=forms.PasswordInput(), validators=[valid_password])
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        cd = self.cleaned_data
        password1 = cd.get('password')
        password2 = cd.get('password2')

        if password1 != password2:
            raise ValidationError(
                _('Passwords doesnt match!!'),
                code='password_match'
            )

        return password2
