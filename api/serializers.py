from rest_framework import serializers
from .models import Page, Block 


class PageSerializer(serializers.ModelSerializer):
    blocks = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'blocks', 'last_update']

    def get_blocks(self, obj):
        blocks = Block.objects.filter(pageId=obj)
        return BlockSerializer(blocks, many=True).data


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'type', 'content', 'settings', 'pageId', "drag_index"]

