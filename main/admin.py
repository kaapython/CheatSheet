from typing import Tuple
from django.contrib import admin
from mptt.admin import MPTTModelAdmin


from .models import *

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    """ Категории тем """
    list_display = (
        "id",
        "name"
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
        "id",
        "name",
        'category',
    )

    list_display_links: Tuple[str] = (
        'name',
    )

    search_fields = (
        'name',
    )