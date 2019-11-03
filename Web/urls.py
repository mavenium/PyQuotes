from django.urls import path, re_path

from Web.views import Index, Persons, QuotesByPerson

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('persons/', Persons.as_view(), name='persons'),
    path('<person_pk>/', QuotesByPerson.as_view(), name='quotes_by_person'),
]
