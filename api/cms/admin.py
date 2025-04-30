from django.contrib import admin

# Register your models here.

from .models import Page, Block

admin.site.register(Page)
admin.site.register(Block)
