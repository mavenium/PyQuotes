from django.urls import path, re_path

from Web.views import Index, Persons

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('persons/', Persons.as_view(), name='persons'),
]
