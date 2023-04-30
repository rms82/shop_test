from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your manager here.
class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone:
            raise ValueError("Users must have a phone")

        user = self.model(
            phone=phone,
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
        user.is_admin = True
        user.save(using=self._db)
        return user


# Create your user model here.
class CustomUser(AbstractBaseUser):
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
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


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
