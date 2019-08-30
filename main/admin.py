from typing import Tuple
from django.contrib import admin

from .models import *

@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    """ Описание тем """
    list_display = ("id", "name")
    list_display_links: Tuple[str] = ('name',)