from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=120, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'


class Cart(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(to='shop.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.title} in cart of {self.cart.user.username}"

    def product_final_price(self):
        return self.quantity * self.product.price

    class Meta:
        verbose_name = 'Корзина товора'
        verbose_name_plural = 'Корзина товора'
