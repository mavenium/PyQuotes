from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=256, verbose_name="Full Name :")
    biography = models.TextField(verbose_name="Biography :")
    picture = models.FileField(verbose_name="Picture :")
