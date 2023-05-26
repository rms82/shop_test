from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import Address, CustomUser
from product.models import Product


# Create your models here.
class Order(models.Model):
    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='order', verbose_name=_("user"))
    total_price = models.IntegerField(default=0, verbose_name=_("total_price"))
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name=_('address'), null=True)
    is_paid = models.BooleanField(default=False, verbose_name=_('is_paid'))

    def __str__(self):
        return f'order for user: {self.user}'


class OrderItem(models.Model):
    class Meta:
        verbose_name = _('orderitem')
        verbose_name_plural = _('orderitems')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item', verbose_name=_("order"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item', verbose_name=_("product"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("quantity"))
    color = models.CharField(max_length=30, verbose_name=_("color"))
    size = models.CharField(max_length=30, verbose_name=_("size"))
    total = models.IntegerField(default=0, verbose_name=_("total"))
