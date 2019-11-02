from django.shortcuts import render
from django.views import generic

from Web.models import Quote


# Create your views here.
class Index(generic.ListView):
    model = Quote
    template_name = 'index.html'
