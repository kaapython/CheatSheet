from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.

from .models import *

def index(request):
    """ Стартовая страница """
    return render_to_response('main/index.html')