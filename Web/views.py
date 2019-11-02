from django.shortcuts import render
from django.views import generic

from Web.models import Quote, Person, Category


# Create your views here.
class Index(generic.ListView):
    model = Quote
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons'] = Person.objects.all()
        context['categories'] = Category.objects.all()
        return context
