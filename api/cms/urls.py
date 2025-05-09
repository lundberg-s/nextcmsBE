from django.urls import path
from .views import (
    PageListCreateView,
    PageDetailView,
    BlockListByPageView,
    BlockListCreateView,
    BlockDetailView,
    BlockOrderUpdateView,
)


urlpatterns = [
    # Pages
    path("pages/", PageListCreateView.as_view(), name="page-list-create"),
    path("pages/<uuid:pk>/", PageDetailView.as_view(), name="page-detail"),
    path("blocks/", BlockListCreateView.as_view(), name="block-list-create"),
    
    
    # Blocks
    path("blocks/<uuid:pk>/", BlockDetailView.as_view(), name="block-detail"),
    path("pages/<uuid:pk>/blocks/", BlockListByPageView.as_view(), name="page-block-list"),
    path("blocks/order/", BlockOrderUpdateView.as_view(), name="block-order-update"),

]
