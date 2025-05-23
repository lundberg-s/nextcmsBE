from rest_framework import serializers
from .models import Page, Block 


class PageSerializer(serializers.ModelSerializer):
    blocks = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'blocks']

    def get_blocks(self, obj):
        blocks = Block.objects.filter(page=obj.id)
        return BlockSerializer(blocks, many=True).data

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'type', 'content', 'style', 'page', "order"]

