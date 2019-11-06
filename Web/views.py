from django.views import generic

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from Web.models import Quote, Person, Category
from Web.serializers import PersonSerializer


# Create your views here.
class Master(generic.ListView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons_widget'] = Person.objects.all()
        context['categories_widget'] = Category.objects.all()
        return context


class Index(Master):
    model = Quote
    ordering = ['-pk']
    paginate_by = 1
    context_object_name = 'quotes_object_list'
    template_name = 'index.html'


class Persons(Master):
    model = Person
    paginate_by = 1
    context_object_name = 'persons_object_list'
    template_name = 'persons.html'


class Random(Index):
    paginate_by = False

    def get_queryset(self):
        return Quote.objects.order_by("?")[:10]


class QuotesByPerson(Index):
    def get_queryset(self):
        return Quote.objects.filter(person=self.kwargs['person_pk'])


class QuotesByCategory(Index):
    def get_queryset(self):
        return Quote.objects.filter(category=self.kwargs['category_pk'])


# REST API Views
class APIPersons(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('-pk')
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



