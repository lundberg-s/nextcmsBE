from django.db import models

# Create your models here.
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

    def save(self, *args, **kwargs):
        if self.drag_index is None:
            last_index = Block.objects.aggregate(models.Max('drag_index'))['drag_index__max']
            self.drag_index = (last_index or 0) + 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['drag_index']

    def __str__(self):
        return self.type