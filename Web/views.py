from django.shortcuts import render
from django.views import generic

from Web.models import Quote, Person, Category


# Create your views here.
class Master(generic.ListView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons'] = Person.objects.all()
        context['categories'] = Category.objects.all()
        return context


class Index(Master):
    model = Quote
    paginate_by = 1
    template_name = 'index.html'


class Persons(Master):
    model = Person
    paginate_by = 1
    template_name = 'persons.html'


class QuotesByPerson(Index):
    def get_queryset(self):
        return Quote.objects.filter(person=self.kwargs['person_pk'])


class QuotesByCategory(Index):
    def get_queryset(self):
        return Quote.objects.filter(category=self.kwargs['category_pk'])
