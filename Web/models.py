from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=256, verbose_name="Full Name :")
    biography = models.TextField(verbose_name="Biography :")
    picture = models.FileField(verbose_name="Picture :", upload_to='persons/')

    def __str__(self):
        return self.full_name


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Category Title :")
    # slug = models.SlugField(max_length=100, verbose_name="Category Slug :")

    def __str__(self):
        return self.title


class Quote(models.Model):
    content = models.TextField(verbose_name="Quote Content :")
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    category = models.OneToOneField(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        pass
