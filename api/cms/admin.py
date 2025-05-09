from django.contrib import admin

# Register your models here.

from cms.models import Page, Block
from user.models import User

admin.site.register(Page)
admin.site.register(Block)
admin.site.register(User)
