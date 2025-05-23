from django.db import models
from root.models import TimestampedModel
import uuid


class Page(TimestampedModel):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, db_index=True, primary_key=True
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    blocks = models.JSONField(default=list)

    def __str__(self):
        return self.title


class Block(TimestampedModel):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, db_index=True, primary_key=True
    )
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    order = models.FloatField(blank=True, null=True)
    content = models.JSONField(default=dict)
    style = models.JSONField(default=dict)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.type
