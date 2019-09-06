from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *
from .forms import *


def index(request, pk=1):
    args = {}
    args['cat'] = Category.objects.all()
    args['category'] = Category.objects.get(id=pk)
    args['description'] = Description.objects.filter(category_id=pk)
    return render_to_response('main/index.html', args)

# def index(request):
#     """ Стартовая страница """
#     cat = Category.objects.all()
#     return render_to_response('main/index.html', {'category': cat})

def category(request):
    """ Вывод описания категории """
    category = Category.objects.all()
    if request.method != 'POST':
        form = AddCategoryForm
    else:
        form = AddCategoryForm(category, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    context = {'form': form, 'category': category, 'category_tree': Category.objects.all()}
    return render(request, 'main/category.html', context)
