from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Page, Block
from .serializers import PageSerializer, BlockSerializer
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)

# Create your views here.

class PageListCreateView(ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.none()
    serializer_class = PageSerializer

    def get_object(self):
        page_id = self.kwargs.get('pk')
        return get_object_or_404(Page, id=page_id)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        page = serializer.save()
        return Response(PageSerializer(page).data)

class BlockListCreateView(ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

class BlockDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def get_object(self):
        block_id = self.kwargs.get('pk')
        return get_object_or_404(Block, id=block_id)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        block = serializer.save()
        return Response(BlockSerializer(block).data)
    

class BlockOrderUpdateView(GenericAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def patch(self, request, *args, **kwargs):
        if not isinstance(request.data, list):
            return Response({"error": "Expected a list of blocks."}, status=status.HTTP_400_BAD_REQUEST)

        blocks = request.data
        block_ids = [b["id"] for b in blocks]
        drag_indices = {b["drag_index"] for b in blocks}

        if len(blocks) != len(drag_indices):
            return Response({"error": "drag_index values must be unique."}, status=status.HTTP_400_BAD_REQUEST)

        block_map = {b.id: b for b in Block.objects.filter(id__in=block_ids)}
        missing_ids = set(block_ids) - set(block_map.keys())

        if missing_ids:
            return Response({"error": f"Blocks with IDs {list(missing_ids)} do not exist."}, status=status.HTTP_400_BAD_REQUEST)

        for block in blocks:
            block_map[block["id"]].drag_index = block["drag_index"]

        Block.objects.bulk_update(block_map.values(), ["drag_index"])
        return Response(BlockSerializer(block_map.values(), many=True).data)
