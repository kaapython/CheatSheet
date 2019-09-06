from django import forms
from .models import *

class AddCategoryForm(forms.ModelForm):
    """ Форма для создания новой задачи """
    class Meta:
        model = Category
        fields = [
            'name',
            'parent',
        ]
        labels = {
            'name': '',
            'parent': '',
        }
#
# class AddDescriptionForm(forms.ModelForm):
#     """ Форма добавления поисания """
#     class Meta:
#         model = Description
#         fields = [
#             'name',
#             'category',
#         ]
#         labels = {
#             'name': '',
#             'category': '',
#         }