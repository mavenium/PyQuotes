from rest_framework import serializers

from Web.models import Person, Category, Quote


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['full_name', 'biography', 'picture', 'pk']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'pk']


class QuoteSerializer(serializers.ModelSerializer):
    person = serializers.StringRelatedField(many=False)
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Quote
        fields = ['content', 'person', 'category', 'pk']
