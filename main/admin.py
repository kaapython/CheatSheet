from typing import Tuple
from django.contrib import admin
from mptt.admin import MPTTModelAdmin, TreeRelatedFieldListFilter


from .models import *

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    """ Категории """
    list_display = (
        'name',
        'id',
    )

    list_display_links: Tuple[str] = (
        'name',
    )

    search_fields = (
        'name',
    )

@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    """ Описание тем """
    list_display = (
        'id',
        'name',
        'category',
        'image',
    )

    list_display_links: Tuple[str] = (
        'name',
    )

    search_fields = (
        'name',
    )
    list_filter = (
        ('category', TreeRelatedFieldListFilter),
    )
    mptt_level_indent = 20