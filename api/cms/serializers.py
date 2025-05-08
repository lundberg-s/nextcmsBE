from rest_framework import serializers
from .models import Page, Block 


class PageSerializer(serializers.ModelSerializer):
    blocks = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'blocks', 'last_update']

    def get_blocks(self, obj):
        # Fetch related blocks for the given page
        blocks = Block.objects.filter(pageId=obj.id)
        return BlockSerializer(blocks, many=True).data

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'type', 'content', 'config', 'pageId', "drag_index"]

