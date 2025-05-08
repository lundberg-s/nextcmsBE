from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    blocks = models.JSONField(default=list)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Block(models.Model):
    type = models.CharField(max_length=100)
    content = models.JSONField(default=dict)
    config = models.JSONField(default=dict)
    pageId = models.ForeignKey(Page, on_delete=models.CASCADE)
    drag_index = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ["drag_index"]

    def __str__(self):
        return self.type
