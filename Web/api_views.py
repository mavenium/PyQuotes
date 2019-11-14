from rest_framework.views import APIView
from rest_framework.response import Response

from Web.models import Category, Person, Quote
from Web.serializers import CategorySerializer, PersonSerializer, QuoteSerializer


class APIPersons(APIView):
    def get(self, request):
        persons_data = Person.objects.all().order_by('-pk')
        return Response(PersonSerializer(persons_data, many=True).data)


class APICategories(APIView):
    def get(self, request):
        categories_data = Category.objects.all().order_by('-pk')
        return Response(CategorySerializer(categories_data, many=True).data)


class APIQuotes(APIView):
    def get(self, request):
        quotes_data = Quote.objects.all().order_by('-pk')
        return Response(QuoteSerializer(quotes_data, many=True).data)


class APIQuotesByPerson(APIView):
    def get(self, request, pk):
        quotes_by_person_data = Quote.objects.filter(person=pk)
        return Response(QuoteSerializer(quotes_by_person_data, many=True).data)


class APIQuotesByCategory(APIView):
    def get(self, request, pk):
        quotes_by_category_data = Quote.objects.filter(category=pk)
        return Response(QuoteSerializer(quotes_by_category_data, many=True).data)


class APIQuotesRandom(APIView):
    def get(self, request):
        quotes_random_data = Quote.objects.order_by('?')[:10]
        return Response(QuoteSerializer(quotes_random_data, many=True).data)
