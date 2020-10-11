from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64)


class Problem(models.Model):
    text = models.TextField()
    categories = models.ManyToManyField(Category, related_name="problems")
    complexity = models.IntegerField(default=1)
