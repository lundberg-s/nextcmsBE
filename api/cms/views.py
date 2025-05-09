from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Page, Block
from django.db.models import Max
from .serializers import PageSerializer, BlockSerializer
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)

class PageListCreateView(ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.none()
    serializer_class = PageSerializer

    def get_object(self):
        page_id = self.kwargs.get('pk')
        return get_object_or_404(Page, id=page_id)
    

class BlockListByPageView(ListAPIView):
    queryset = Block.objects.none()
    serializer_class = BlockSerializer

    def get_queryset(self):
        page_id = self.kwargs.get('pk')
        return Block.objects.filter(page=page_id)


class BlockListCreateView(ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def perform_create(self, serializer):
        last_index = Block.objects.aggregate(Max("order"))["order__max"]
        serializer.save(order=(last_index or 0) + 1)

        super().perform_create(serializer)
        

class BlockDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def get_object(self):
        block_id = self.kwargs.get('pk')
        return get_object_or_404(Block, id=block_id)
    

class BlockOrderUpdateView(GenericAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

    def patch(self, request, *args, **kwargs):
        if not isinstance(request.data, list):
            return Response({"error": "Expected a list of blocks."}, status=status.HTTP_400_BAD_REQUEST)

        # Update blocks in bulk
        Block.objects.bulk_update(
            [Block(id=block["id"], order=block["order"]) for block in request.data],
            ["order"]
        )
        return Response({"message": "Blocks updated successfully."}, status=status.HTTP_200_OK)
