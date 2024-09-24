from topshiriq1 import serializers
from topshiriq5.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=("title","content",'user')
        read_only_fields=('id',)
