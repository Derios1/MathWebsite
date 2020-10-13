from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Problem(models.Model):
    title = models.CharField(max_length=128, default="")
    text = models.TextField()
    categories = models.ManyToManyField(Category, related_name="problems")
    complexity = models.IntegerField(default=1)

    answer = models.CharField(max_length=128, default="0")

    # Symbols which are used in answer formula.
    # Format of field: "sym_1 sym_2 sym_3 ... "
    symbols = models.CharField(max_length=128, default="", blank=True)

    def __str__(self):
        return self.title
