from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


# Create your manager here.
class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        """
        Creates and saves a User with the given phone and password.
        """
        if not phone:
            raise ValueError("Users must have a phone")

        user = self.model(
            phone=phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# Create your user model here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = _('CustomUser')
        verbose_name_plural = _('CustomUsers')

    phone = models.CharField(max_length=12, unique=True, verbose_name=_('Phone Number'))
    email = models.EmailField(
        verbose_name=_("email address"),
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    fullname = models.CharField(max_length=128, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone


def has_rosetta_access(user):
    return True


class OTP(models.Model):
    class Meta:
        verbose_name = _('OTP')
        verbose_name_plural = _('OTPS')

    token = models.CharField(max_length=10)
    otp = models.SmallIntegerField()
    phone = models.CharField(max_length=11)

    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


class Address(models.Model):
    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='address', verbose_name=_('user'))
    fullname = models.CharField(max_length=50, verbose_name=_('fullname'))
    email = models.EmailField(blank=True, null=True, verbose_name=_('email'))
    code_post = models.CharField(max_length=12, verbose_name=_("code_post"))
    phone = models.CharField(max_length=12, verbose_name=_("phone"))
    address = models.TextField(verbose_name=_('address'))

    def __str__(self):
        return self.user.phone
