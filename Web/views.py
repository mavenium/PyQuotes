from django.views import generic

from Web.models import Quote, Person, Category


# Create your views here.
class Master(generic.ListView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons_widget'] = Person.objects.all()
        context['categories_widget'] = Category.objects.all()
        return context


class Index(Master):
    model = Quote
    paginate_by = 1
    context_object_name = 'quotes_object_list'
    template_name = 'index.html'


class Persons(Master):
    model = Person
    paginate_by = 1
    context_object_name = 'persons_object_list'
    template_name = 'persons.html'


class Random(Index):
    def get_queryset(self):
        return Quote.objects.order_by("?")


class QuotesByPerson(Index):
    def get_queryset(self):
        return Quote.objects.filter(person=self.kwargs['person_pk'])


class QuotesByCategory(Index):
    def get_queryset(self):
        return Quote.objects.filter(category=self.kwargs['category_pk'])
