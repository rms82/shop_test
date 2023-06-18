from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


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
    description = RichTextField(verbose_name=_('description'))

    price = models.IntegerField(verbose_name=_('price'))
    off = models.SmallIntegerField(verbose_name=_('off'), null=True, blank=True,
                                   help_text=_("off should less than 60%."))

    image = models.ImageField(upload_to='products/', verbose_name=_('image'))
    color = models.ManyToManyField(Color, verbose_name=_('color'), blank=True)
    size = models.ManyToManyField(Size, verbose_name=_('size'), blank=True)
    category = models.ManyToManyField('Category', verbose_name=_('category'), blank=True)

    def __str__(self):
        return self.title


class ProductFeature(models.Model):
    class Meta:
        verbose_name = _("Product Feature")
        verbose_name_plural = _('Product Features')

    title = models.CharField(max_length=128, verbose_name=_('title'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='features', verbose_name=_('product'))

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _('Categories')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subs', verbose_name=_('parent'),
                               null=True, blank=True)
    name = models.CharField(max_length=32, verbose_name=_('name'))

    def __str__(self):
        return self.name
