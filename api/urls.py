from django.urls import path
from .views import (
    PageBlockListView,
    PageListCreateView,
    PageDetailView,
    BlockListCreateView,
    BlockDetailView,
    BlockOrderUpdateView,
)


urlpatterns = [
    path("pages/", PageListCreateView.as_view(), name="page-list-create"),
    path("pages/<int:pk>/", PageDetailView.as_view(), name="page-detail"),
    path("blocks/", BlockListCreateView.as_view(), name="block-list-create"),
    path("blocks/<int:pk>/", BlockDetailView.as_view(), name="block-detail"),
    path("blocks/order/", BlockOrderUpdateView.as_view(), name="block-order-update"),
    path("blocks/page/<int:pk>/", PageBlockListView.as_view(), name="page-block-list"),
]
