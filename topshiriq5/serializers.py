from topshiriq1 import serializers
from topshiriq5.models import Post, Product


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "content", "user")
        read_only_fields = ("id",)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('__all__')
        read_only_fields = ("id",)