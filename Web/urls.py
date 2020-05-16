from django.urls import path

from Web.views import Index, Persons, Random, QuotesByPerson, QuotesByCategory, CategoryCreateView, PersonCreateView, QuoteCreateView, LogoutView
from Web.api_views import APIPersons, APICategories, APIQuotes, APIQuotesByPerson, APIQuotesByCategory, APIQuotesRandom

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('persons/', Persons.as_view(), name='persons'),
    path('create/category', CategoryCreateView.as_view(), name='create_category'),
    path('create/person', PersonCreateView.as_view(), name='create_person'),
    path('create/quote', QuoteCreateView.as_view(), name='create_quote'),
    path('qbp/<person_pk>/', QuotesByPerson.as_view(), name='quotes_by_person'),
    path('qbc/<category_pk>/', QuotesByCategory.as_view(), name='quotes_by_category'),
    path('random/', Random.as_view(), name='random'),
    path('account/logout', LogoutView.as_view(), name='logout'),
    path('api/persons/', APIPersons.as_view(), name="api_persons"),
    path('api/categories/', APICategories.as_view(), name="api_categories"),
    path('api/quotes/', APIQuotes.as_view(), name="api_quotes"),
    path('api/qbp/<int:pk>/', APIQuotesByPerson.as_view(), name="api_quotes_by_person"),
    path('api/qbc/<int:pk>/', APIQuotesByCategory.as_view(), name="api_quotes_by_category"),
    path('api/quotes_random/', APIQuotesRandom.as_view(), name="api_quotes_random"),
]
