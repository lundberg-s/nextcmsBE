from django.db.models import Max
from .models import Block

def get_next_drag_index():
    """Utility function to calculate the next drag index."""
    last_index = Block.objects.aggregate(Max("drag_index"))["drag_index__max"]
    return (last_index or 0) + 1