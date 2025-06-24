from rest_framework import serializers

from shop.models import Feedback, FavoriteProduct, Product


class CategoryListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class SizeListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class ProductImageSerializer(serializers.Serializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url if obj.image else None
        return request.build_absolute_uri(image_url) if image_url else None


class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        first_image = obj.product_images.first()
        if first_image:
            return ProductImageSerializer(first_image, context=self.context).data
        else:
            return None


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
        read_only_fields = ["created_at"]


class FavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProduct
        fields = "__all__"
        read_only_fields = ["created_at"]



class ProductDetailSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    price_with_discount = serializers.FloatField(read_only=True)


    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'sale',
            'discount_percent',
            'price_with_discount',
            'sizes',
            'category',
            'tags',
            'long_description',
            'product_images'
        ]