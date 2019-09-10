from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField

# Create your models here.

class Category(MPTTModel):
    """ Иерархическая структура категорий тем """
    name = models.CharField('Категория', max_length=50, unique=True, help_text='Категория')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родитель', help_text='Родитель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    class MPTTMeta:
        order_insertion_by = ['name']


class Description(models.Model):
    """ Описание тем, вопросов """
    name = RichTextField(verbose_name='Описание', help_text='Описание')
    category = TreeForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='category', verbose_name='Категория', help_text='Категория')
    image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Изображение')
    def __str__(self):
        return format(self.name)

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'
        ordering = ['id']