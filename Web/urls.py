from django.urls import path, re_path, include

from rest_framework import routers

from Web.views import Index, Persons, Random, QuotesByPerson, QuotesByCategory, APIPersons

router = routers.DefaultRouter()
router.register(r'persons', APIPersons)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('persons/', Persons.as_view(), name='persons'),
    path('qbp/<person_pk>/', QuotesByPerson.as_view(), name='quotes_by_person'),
    path('qbc/<category_pk>/', QuotesByCategory.as_view(), name='quotes_by_category'),
    path('random/', Random.as_view(), name='random'),
    path('api/', include(router.urls)),
]
