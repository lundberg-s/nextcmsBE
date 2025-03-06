

from django.urls import path
from .views import PageListCreateView, PageDetailView, BlockListCreateView, BlockDetailView, BlockOrderUpdateView


urlpatterns = [
    path("pages/", PageListCreateView.as_view(), name="page-list-create"),
    path("pages/<int:pk>/", PageDetailView.as_view(), name="page-detail"),
    path("blocks/", BlockListCreateView.as_view(), name="block-list-create"),
    path("blocks/<int:pk>/", BlockDetailView.as_view(), name="block-detail"),
    path("blocks/order/", BlockOrderUpdateView.as_view(), name="block-order-update"),

]
