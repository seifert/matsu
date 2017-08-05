
from django.contrib import admin

from matsu.core.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'tree_path')
    ordering = ('id',)
    search_fields = ('title',)

    class Media:
        css = {
            "all": (
                "css/simplemde.min.css",
                "css/admin/core/category/simplemde.css",
            )
        }
        js = (
            "js/simplemde.min.js",
            'js/admin/core/category/simplemde.js',
        )
