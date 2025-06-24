from django.db import models

from user.models import CustomUser

class Category(models.Model):
    title = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


class ProductSize(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    title = models.CharField(max_length=10, choices=SIZE_CHOICES)

    def __str__(self):
        return self.title


class ProductTags(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория тега'
        verbose_name_plural = 'Категория тега'


class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.FloatField()
    sale = models.BooleanField(default=False)
    discount_percent = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    short_description = models.TextField()
    sizes = models.ManyToManyField(ProductSize)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(ProductTags)
    long_description = models.TextField()

    def __str__(self):
        return self.title

    @property
    def price_with_discount(self):
        discount_amount = self.discount_percent * (self.price / 100)
        return self.price - discount_amount

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"ID: {self.id}| Product: {self.product.title}"

    class Meta:
        verbose_name = 'Товар-фото'
        verbose_name_plural = 'Товар-фото'


# ---------------------------------------------------------------------------------
# Feedback

class Feedback(models.Model):
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Добавить изб'
        verbose_name_plural = 'Добавить изб'


class FavoriteProduct(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Добавить корзину'
        verbose_name_plural = 'Добавить корзину'