from django.contrib import admin

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ("tags",)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Tag)
