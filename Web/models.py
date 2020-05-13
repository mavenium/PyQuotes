from django.db import models
from django.urls import reverse


class Person(models.Model):
    full_name = models.CharField(max_length=256, verbose_name="Full Name :")
    biography = models.TextField(verbose_name="Biography :")
    picture = models.FileField(verbose_name="Picture :", upload_to='persons/')

    @staticmethod
    def get_absolute_url():
        return reverse("create_person")

    def __str__(self):
        return self.full_name


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Category Title :")
    # slug = models.SlugField(max_length=100, verbose_name="Category Slug :")

    @staticmethod
    def get_absolute_url():
        return reverse("create_category")

    def __str__(self):
        return self.title


class Quote(models.Model):
    content = models.TextField(verbose_name="Quote Content :")
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    @staticmethod
    def get_absolute_url():
        return reverse("create_quote")

    def display_category(self):
        return ', '.join([cat.title for cat in self.category.all()])

    def __str__(self):
        return self.content
