from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

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


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView, Master):
    fields = ["title"]
    model = Category
    success_url = '/create/category'
    success_message = "Category was created successfully"


class PersonCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView, Master):
    fields = ["full_name", "biography", "picture"]
    model = Person
    success_url = '/create/person'
    success_message = 'Person was created successfully'


class QuoteCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView, Master):
    fields = ["person", "category", "content"]
    model = Quote
    success_url = '/create/quote'
    success_message = 'Quote was created successfully'


class LogoutView(generic.RedirectView):
    url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
