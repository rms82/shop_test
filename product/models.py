from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Size(models.Model):
    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')

    size = models.CharField(max_length=16, verbose_name=_('size'))

    def __str__(self):
        return self.size


class Color(models.Model):
    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')

    color = models.CharField(max_length=32, verbose_name=_('color'))

    def __str__(self):
        return self.color


class Product(models.Model):
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    title = models.CharField(max_length=128, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))

    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('price'))
    off = models.SmallIntegerField(verbose_name=_('off'), null=True, blank=True)

    image = models.ImageField(upload_to='products/', verbose_name=_('image'))
    color = models.ManyToManyField(Color, verbose_name=_('color'), blank=True)
    size = models.ManyToManyField(Size, verbose_name=_('size'),blank=True)

    def __str__(self):
        return self.title
